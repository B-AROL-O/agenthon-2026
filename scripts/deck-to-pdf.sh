#!/bin/bash
# ==========================================================
# Export the pitch deck to a PDF with one 1920x1080 slide per page, without
# the export header, slide numbers or speaker notes.
#
# Prints a copy of the deck, with print CSS added, in headless Chromium or
# Chrome. The copy sits next to the deck so the relative img/ paths resolve,
# and is removed afterwards.
#
# Usage: scripts/deck-to-pdf.sh [OUTPUT.pdf]
#        (default: build/track2-pitch-deck.pdf)
#
# Environment:
#   CHROME  Chromium or Chrome binary (default: the first one found on PATH)
# ==========================================================

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DECK="$REPO_ROOT/docs/slides/track2-pitch-deck.html"
OUTPUT="${1:-$REPO_ROOT/build/track2-pitch-deck.pdf}"

if [ -z "${CHROME:-}" ]; then
	for c in chromium chromium-browser google-chrome google-chrome-stable; do
		if command -v "$c" >/dev/null 2>&1; then
			CHROME="$c"
			break
		fi
	done
fi
if [ -z "${CHROME:-}" ]; then
	echo "ERROR: Chromium or Chrome not found; set CHROME to its path" >&2
	exit 1
fi

PRINT_CSS='<style>
@page { size: 1920px 1080px; margin: 0; }
html, body { margin: 0 !important; padding: 0 !important; background: none !important; }
.export-header, .slide-num, .notes { display: none !important; }
main { margin: 0; padding: 0; }
.slide-wrap { max-width: none !important; width: 1920px; height: 1080px; margin: 0 !important; break-after: page; overflow: hidden; }
.slide-wrap:last-child { break-after: auto; }
.stage { width: 1920px !important; height: 1080px !important; border-radius: 0 !important; --s: 1 !important; }
.stage > section { transform: none !important; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
</style>'

if [ "$(grep -c '</head>' "$DECK")" -ne 1 ]; then
	echo "ERROR: expected exactly one </head> in $DECK" >&2
	exit 1
fi

print_copy="$(mktemp --suffix=.html "$(dirname "$DECK")/.print-XXXXXX")"
trap 'rm -f "$print_copy"' EXIT
PRINT_CSS="$PRINT_CSS" awk '/<\/head>/ { print ENVIRON["PRINT_CSS"] } { print }' "$DECK" >"$print_copy"

mkdir -p "$(dirname "$OUTPUT")"
# The time budget lets the Google Fonts and images load before printing
"$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
	--virtual-time-budget=15000 --print-to-pdf="$OUTPUT" "file://$print_copy" 2>/dev/null

if [ ! -s "$OUTPUT" ]; then
	echo "ERROR: $CHROME did not write $OUTPUT" >&2
	exit 1
fi
echo "Wrote $OUTPUT"

# EOF
