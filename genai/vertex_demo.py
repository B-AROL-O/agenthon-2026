"""Minimal Gemini / Nano Banana / Veo examples on Vertex AI (Agent Platform API).

Every call goes through Vertex AI with your project + Application Default
Credentials, so it is billed to the project's billing account (and its free
credits). Nothing here uses an AI Studio API key.

Usage:
    uv run vertex_demo.py text  "Write a tagline for a hand-rolled breadstick"
    uv run vertex_demo.py image "A grissino on a marble aperitivo table" [--full]
        [--ref photo.jpg --ref pack.png] [--size 2K] [--aspect-ratio 4:5] [--name hero]
    uv run vertex_demo.py video "Grissino snapping in half" [--final] [--audio] [--seconds 6]
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

from google import genai
from google.genai import errors, types

# --- Models (GA only, never -preview) ---------------------------------------
TEXT_MODEL = "gemini-3.8-flash"  # cheapest GA Gemini until 31 Dec
IMAGE_MODEL_LITE = "gemini-3.1-flash-lite-image"  # Nano Banana 2 Lite (half price)
IMAGE_MODEL_FULL = "gemini-3.1-flash-image"  # Nano Banana 2
VIDEO_MODEL_DRAFT = "veo-3.1-fast-generate-001"  # Veo 3.1 Fast (1/4 price)
VIDEO_MODEL_FINAL = "veo-3.1-generate-001"  # Veo 3.1

# --- Locations --------------------------------------------------------------
# Gemini 3.x text/image models are served on the "global" endpoint.
GEMINI_LOCATION = os.environ.get("GEMINI_LOCATION", "global")
# Veo runs only in us-central1.
VEO_LOCATION = "us-central1"

OUT_DIR = Path(__file__).parent / "out"


def _project() -> str:
    project = os.environ.get("GOOGLE_CLOUD_PROJECT")
    if not project:
        sys.exit("Set GOOGLE_CLOUD_PROJECT to your project ID (see README).")
    return project


def _client(location: str) -> genai.Client:
    # Make sure no AI Studio key sneaks in: the credits don't cover AI Studio.
    for var in ("GOOGLE_API_KEY", "GEMINI_API_KEY"):
        if os.environ.pop(var, None):
            print(f"[warn] ignoring {var}: using Vertex AI + ADC instead", file=sys.stderr)
    return genai.Client(enterprise=True, project=_project(), location=location)


def _check_model(model: str) -> None:
    if "preview" in model:
        sys.exit(f"Refusing {model}: -preview models are not covered by the credits.")


# --- Text -------------------------------------------------------------------
def run_text(prompt: str) -> None:
    """Generate text with Gemini."""
    _check_model(TEXT_MODEL)
    client = _client(GEMINI_LOCATION)
    resp = client.models.generate_content(model=TEXT_MODEL, contents=prompt)
    print(resp.text)
    if resp.usage_metadata:
        u = resp.usage_metadata
        print(
            f"\n[tokens] in={u.prompt_token_count} out={u.candidates_token_count}", file=sys.stderr
        )


# --- Image (Nano Banana) ----------------------------------------------------
IMAGE_RETRY_PAUSE_S = 65  # quota is ~1 request/minute/project
IMAGE_MAX_ATTEMPTS = 4


REF_MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}


def _ref_part(path: str) -> types.Part:
    """Load a local reference image (product photo, pack front) as an input part."""
    ref = Path(path)
    mime = REF_MIME.get(ref.suffix.lower())
    if not mime:
        sys.exit(f"Unsupported reference image type: {ref}")
    return types.Part.from_bytes(data=ref.read_bytes(), mime_type=mime)


def run_image(  # pylint: disable=too-many-locals,too-many-arguments,too-many-positional-arguments
    prompt: str,
    full: bool,
    aspect_ratio: str,
    refs: list[str] | None = None,
    size: str = "1K",
    name: str = "image",
) -> None:
    """Generate one image with Nano Banana, optionally guided by reference images."""
    model = IMAGE_MODEL_FULL if full else IMAGE_MODEL_LITE
    _check_model(model)
    client = _client(GEMINI_LOCATION)
    config = types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        image_config=types.ImageConfig(aspect_ratio=aspect_ratio, image_size=size),
    )
    contents: list = [_ref_part(r) for r in refs or []] + [prompt]
    print(f"[image] {model}, {size}, {aspect_ratio}, {len(refs or [])} ref(s)", file=sys.stderr)

    for attempt in range(1, IMAGE_MAX_ATTEMPTS + 1):
        try:
            resp = client.models.generate_content(model=model, contents=contents, config=config)
            break
        except errors.ClientError as e:
            if e.code != 429 or attempt == IMAGE_MAX_ATTEMPTS:
                raise
            print(
                f"[429] quota hit, waiting {IMAGE_RETRY_PAUSE_S}s (attempt {attempt})",
                file=sys.stderr,
            )
            time.sleep(IMAGE_RETRY_PAUSE_S)

    cand = resp.candidates[0] if resp.candidates else None
    parts = (cand.content.parts if cand and cand.content else None) or []

    OUT_DIR.mkdir(exist_ok=True)
    saved = 0
    for part in parts:
        if part.inline_data and part.inline_data.data:
            ext = (part.inline_data.mime_type or "image/png").split("/")[-1]
            path = OUT_DIR / f"{name}_{int(time.time())}_{saved}.{ext}"
            path.write_bytes(part.inline_data.data)
            print(f"saved {path}")
            saved += 1
        elif part.text:
            print(part.text)
    if not saved:
        reason = cand.finish_reason if cand else None
        sys.exit(
            f"No image returned (finish_reason={reason}, prompt_feedback={resp.prompt_feedback})."
        )
    print(f"[note] wait ~{IMAGE_RETRY_PAUSE_S}s before the next image request.", file=sys.stderr)


# --- Video (Veo) ------------------------------------------------------------
def run_video(prompt: str, final: bool, audio: bool, seconds: int, aspect_ratio: str) -> None:
    """Generate one Veo clip and save it as MP4."""
    model = VIDEO_MODEL_FINAL if final else VIDEO_MODEL_DRAFT
    _check_model(model)
    client = _client(VEO_LOCATION)
    print(
        f"[veo] {model}, {seconds}s, audio={'on' if audio else 'off'}, {aspect_ratio}",
        file=sys.stderr,
    )

    op = client.models.generate_videos(
        model=model,
        prompt=prompt,
        config=types.GenerateVideosConfig(
            number_of_videos=1,
            duration_seconds=seconds,
            generate_audio=audio,
            aspect_ratio=aspect_ratio,
            resolution="720p",
            # No output_gcs_uri: the video bytes come back inline, so .save() works.
        ),
    )
    while not op.done:
        time.sleep(15)
        op = client.operations.get(op)
        print("[veo] still generating...", file=sys.stderr)

    if op.error:
        sys.exit(f"Veo error: {op.error}")
    result = op.response or op.result
    if not result or not result.generated_videos:
        reasons = getattr(result, "rai_media_filtered_reasons", None) if result else None
        sys.exit(f"No video returned (safety filter?): {reasons}")

    OUT_DIR.mkdir(exist_ok=True)
    path = OUT_DIR / f"video_{int(time.time())}.mp4"
    result.generated_videos[0].video.save(str(path))
    print(f"saved {path}")


def main() -> None:
    """Parse the CLI and dispatch to a subcommand."""
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    t = sub.add_parser("text", help=f"Gemini text ({TEXT_MODEL})")
    t.add_argument("prompt")

    i = sub.add_parser("image", help=f"Nano Banana image ({IMAGE_MODEL_LITE} by default)")
    i.add_argument("prompt")
    i.add_argument("--full", action="store_true", help=f"use {IMAGE_MODEL_FULL} (2x price)")
    i.add_argument("--aspect-ratio", default="1:1")
    i.add_argument("--ref", action="append", default=[], help="reference image path (repeatable)")
    i.add_argument("--size", choices=["1K", "2K", "4K"], default="1K")
    i.add_argument("--name", default="image", help="output file prefix")

    v = sub.add_parser("video", help=f"Veo clip ({VIDEO_MODEL_DRAFT} by default)")
    v.add_argument("prompt")
    v.add_argument("--final", action="store_true", help=f"use {VIDEO_MODEL_FINAL} (4x price)")
    v.add_argument("--audio", action="store_true", help="generate audio (2x price)")
    v.add_argument("--seconds", type=int, choices=[4, 6], default=4)
    v.add_argument("--aspect-ratio", choices=["16:9", "9:16"], default="16:9")

    a = p.parse_args()
    if a.cmd == "text":
        run_text(a.prompt)
    elif a.cmd == "image":
        run_image(a.prompt, a.full, a.aspect_ratio, a.ref, a.size, a.name)
    else:
        run_video(a.prompt, a.final, a.audio, a.seconds, a.aspect_ratio)


if __name__ == "__main__":
    main()
