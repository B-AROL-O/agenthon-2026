#!/bin/bash
# ==========================================================
# Publish the Track 2 deliverables to the submission Google Drive folder.
#
# Each owner publishes their own part from their own machine:
#   spot    01-spot/                    Luca     (folder given with --spot-dir)
#   static  02-social/ 03-web-print/    Alessio  (genai/out/drive/, from `uv run campaign.py`)
#           04-ad-image/
#   docs    05-project-sheet/           anyone   (rendered from docs/ in this repository)
#           06-tools-list/
#
# Uses `rclone copy`: it adds and updates files, and never deletes anything in
# Drive. Without --run it only shows what it would do (rclone --dry-run).
#
# Usage: scripts/publish-to-drive.sh [--run] [--spot-dir DIR] [--force-late] <spot|static|docs|all>...
#
# Environment:
#   DRIVE_REMOTE     rclone remote for Google Drive (default: gdrive:)
#   DRIVE_FOLDER_ID  ID of the submission folder (default: the team's folder)
#
# See docs/howto-publish-to-drive.md for the one-time rclone setup.
# ==========================================================

set -euo pipefail

DRIVE_REMOTE="${DRIVE_REMOTE:-gdrive:}"
DRIVE_FOLDER_ID="${DRIVE_FOLDER_ID:-1mL-yWZ0gsObf_6VHV3TmJgGfv0_Wswkp}"
# The team freezes the folder at 16:45 (docs/track2-wbs.md); --force-late allows
# an emergency fix until 16:59. Drive records file timestamps at 17:00, and a
# file changed after that no longer counts, so nothing is ever uploaded later.
FREEZE="16:45"
DEADLINE="16:59"

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BUILD_DIR="$REPO_ROOT/build/drive"
STATIC_DIR="$REPO_ROOT/genai/out/drive"

usage() {
	sed -n '3,21p' "$0" | sed 's/^# \{0,1\}//'
}

run=0
force_late=0
spot_dir=""
parts=()

while [ $# -gt 0 ]; do
	case "$1" in
	--run)
		run=1
		shift
		;;
	--force-late)
		force_late=1
		shift
		;;
	--spot-dir)
		[ $# -ge 2 ] || {
			echo "ERROR: --spot-dir requires a directory" >&2
			exit 1
		}
		spot_dir="$2"
		shift 2
		;;
	-h | --help)
		usage
		exit 0
		;;
	spot | static | docs)
		parts+=("$1")
		shift
		;;
	all)
		parts+=(spot static docs)
		shift
		;;
	*)
		echo "ERROR: Unknown argument: $1" >&2
		usage >&2
		exit 1
		;;
	esac
done

if [ ${#parts[@]} -eq 0 ]; then
	usage >&2
	exit 1
fi

if ! command -v rclone >/dev/null 2>&1; then
	echo "ERROR: rclone is not installed; see docs/howto-publish-to-drive.md" >&2
	exit 1
fi

if ! rclone listremotes | grep -qx "${DRIVE_REMOTE%%:*}:"; then
	echo "ERROR: rclone remote '$DRIVE_REMOTE' not found; run 'rclone config' (see docs/howto-publish-to-drive.md)" >&2
	exit 1
fi

now="$(TZ=Europe/Rome date +%H:%M)"
if [ "$run" -eq 1 ] && [[ "$now" > "$DEADLINE" ]]; then
	echo "ERROR: it is $now in Torino: an upload now would change files after the 17:00 deadline." >&2
	exit 1
fi
if [ "$run" -eq 1 ] && [ "$force_late" -eq 0 ] && [[ "$now" > "$FREEZE" ]]; then
	echo "ERROR: it is $now in Torino: the submission folder froze at $FREEZE." >&2
	echo "       Pass --force-late for an emergency fix agreed with the team (until $DEADLINE)." >&2
	exit 1
fi

rclone_flags=(--drive-root-folder-id "$DRIVE_FOLDER_ID" --verbose)
[ "$run" -eq 1 ] || rclone_flags+=(--dry-run)

# copy_dir <local dir> <Drive subfolder> [extra rclone flags...]
copy_dir() {
	local src="$1" dest="$2"
	shift 2
	if [ ! -d "$src" ]; then
		echo "ERROR: $src does not exist" >&2
		exit 1
	fi
	echo "==> $src -> $DRIVE_REMOTE$dest/"
	rclone copy "$src" "$DRIVE_REMOTE$dest" "${rclone_flags[@]}" "$@"
}

publish_spot() {
	if [ -z "$spot_dir" ]; then
		echo "ERROR: 'spot' needs --spot-dir DIR, the folder with the final spot exports" >&2
		exit 1
	fi
	copy_dir "$spot_dir" "01-spot"
}

publish_static() {
	local d
	for d in 02-social 03-web-print 04-ad-image; do
		copy_dir "$STATIC_DIR/$d" "$d"
	done
}

# render_doc <docs/file.md> <Drive subfolder>: PDF with publish-md-pdf, DOCX with
# the pandoc in the same image; Drive imports the DOCX as a Google Doc.
render_doc() {
	local md="$1" dest="$2" name out
	name="$(basename "$md" .md)"
	out="$BUILD_DIR/$dest"
	rm -rf "$out"
	mkdir -p "$out/pdf" "$out/gdoc"
	(cd "$REPO_ROOT" && scripts/publish-md-pdf.sh --output-dir "build/drive/$dest/pdf" "$md")
	(cd "$REPO_ROOT" && docker run --rm --user "$(id -u):$(id -g)" -e HOME=/tmp \
		-v "$REPO_ROOT:/workspace" --entrypoint pandoc \
		"${PUBLISH_MD_PDF_IMAGE:-ghcr.io/b-arol-o/publish-md-pdf:v2}" \
		"$md" --output "build/drive/$dest/gdoc/$name.docx")
}

publish_docs() {
	render_doc docs/track2-project-sheet.md 05-project-sheet
	render_doc docs/track2-tools.md 06-tools-list
	local dest
	for dest in 05-project-sheet 06-tools-list; do
		copy_dir "$BUILD_DIR/$dest/pdf" "$dest"
		copy_dir "$BUILD_DIR/$dest/gdoc" "$dest" --drive-import-formats docx
	done
}

for part in "${parts[@]}"; do
	"publish_$part"
done

if [ "$run" -eq 0 ]; then
	echo "Dry run only: nothing was uploaded. Add --run to publish."
fi

# EOF
