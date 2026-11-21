# Gemini, Nano Banana and Veo on Vertex AI

Every call goes through Vertex AI (now named "Agent Platform API", `aiplatform.googleapis.com`) and uses your project and Application Default Credentials.
Because of that, the cost goes to the billing account that holds the hackathon credits.
Do not use the Gemini API in Google AI Studio or an AI Studio API key: the credits don't cover them.

## One-time setup (macOS)

```bash
# 1. Install and log in
brew install --cask google-cloud-sdk
gcloud auth login

# 2. Create the project (the ID must be globally unique)
export PROJECT_ID=agenthon-2026-$RANDOM
gcloud projects create "$PROJECT_ID"
gcloud config set project "$PROJECT_ID"

# 3. Link it to the billing account that holds the $30 credits
gcloud billing accounts list                     # pick the right ACCOUNT_ID
gcloud billing projects link "$PROJECT_ID" --billing-account=XXXXXX-XXXXXX-XXXXXX
gcloud billing projects describe "$PROJECT_ID"   # expect billingEnabled: true

# 4. Enable the Vertex AI (Agent Platform) API
gcloud services enable aiplatform.googleapis.com

# 5. Application Default Credentials for the SDK
gcloud auth application-default login
gcloud auth application-default set-quota-project "$PROJECT_ID"

# 6. Tell the script which project to use
export GOOGLE_CLOUD_PROJECT="$PROJECT_ID"
unset GOOGLE_API_KEY GEMINI_API_KEY             # never bill through AI Studio
```

Optional: set a budget alert in the console under Billing → Budgets & alerts, at about $25.
An alert only notifies you; it does not stop spending.
The credit balance takes about an hour to update, so the alert lags behind by that much too.

## Run

```bash
cd genai
uv sync

uv run vertex_demo.py text  "Three taglines for Rubatà breadsticks at aperitivo"
uv run vertex_demo.py image "Rubatà grissini on a marble table, golden hour"   # Lite (cheapest)
uv run vertex_demo.py image "..." --full --aspect-ratio 9:16                   # Nano Banana 2
uv run vertex_demo.py video "Slow-motion grissino snapping in half"             # Fast, 4s, no audio
uv run vertex_demo.py video "..." --final --seconds 6 --audio                   # final clip
```

The script saves output to `genai/out/`, which Git ignores.

## Cost defaults built into the script

| What  | Default                                                  | Opt-in (costs more)                                                    |
| ----- | -------------------------------------------------------- | ---------------------------------------------------------------------- |
| Text  | `gemini-3.8-flash`, location `global`                    | none                                                                   |
| Image | `gemini-3.1-flash-lite-image` at 1K                      | `--full` → `gemini-3.1-flash-image` (2×)                               |
| Video | `veo-3.1-fast-generate-001`, 4 s, 720p, no audio, 1 clip | `--final` → `veo-3.1-generate-001` (4×); `--audio` (2×); `--seconds 6` |

- Veo always runs in `us-central1` with the project passed explicitly. An API key alone fails with `RESOURCE_PROJECT_INVALID`.
- Nano Banana allows about one request per minute per project. On a 429 error the script waits 65 s and retries, up to 4 attempts. Leave about a minute between image runs.
- The script refuses any model ID that contains `preview`.

## WP2 static visuals

Pipeline for [issue #9](https://github.com/B-AROL-O/agenthon-2026/issues/9): Nano Banana generates text-free plates, then `compose.py` adds everything readable with Pillow.
Logos, packshots and the pack window come from the official kit files (`assets/feyles/`), never from the model.

```bash
# Plates: prompts live in prompts/, reference photos are passed with --ref (repeatable)
uv run vertex_demo.py image "$(cat prompts/hero-ad-4x5.txt)" --full --size 2K --aspect-ratio 4:5 \
  --name hero-full --ref ../assets/feyles/05_IMMAGINI_2048/Grissini/CLASSICO_MAX1896.jpg

# Composites: one layout per deliverable ID, output in out/final/
uv run compose.py --list
uv run compose.py hero-ad-4x5 --plate out/hero-full_<ts>_0.png --variant band
uv run compose.py print-poster-2x3 --plate out/poster-spiga-full_<ts>_0.png --plate out/poster-rubata-full_<ts>_0.png
uv run compose.py social-finestra-1x1   # no AI: real Classico photo behind the official die-cut window
```

- Workflow: draft each plate on Lite at 1K, then render the approved prompt once on Full at 2K (4K for the poster).
- `uv run compose.py --make-refs` writes `out/refs/classico-sticks-crop.jpg`, a tight crop of the kit's Classico photo with almost no slate, so the model doesn't copy the dark background. Pass it with `--ref`.
- Scenes with people never show a readable pack: the real 3D mockup is placed as a packshot in the flat colour block.
- Outputs contain Feyles marks and stay out of Git (`out/` is ignored); final files go to the Drive folder.

### Fonts

- **Titles: Playfair Display** (SIL Open Font License, in `fonts/`).
  The brand typeface **Alga** is a commercial font that is not included in the client kit; the identity guide names Didot or Playfair Display as the alternatives.
  We used Playfair Display because it is free and the whole team can reproduce the output.
- **Body and CTAs: Lato** (SIL Open Font License, in `fonts/`), the brand's official text font.

## Not covered by the credits

These are billed to you, so avoid them:

- Marketplace and partner models
- GKE
- GPUs and TPUs
- Spot VMs
- Any `-preview` model

<!-- EOF -->
