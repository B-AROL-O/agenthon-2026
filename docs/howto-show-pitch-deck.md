# HOWTO Show the pitch deck

<!-- (2026-11-21) -->

The [pitch deck](slides/track2-pitch-deck.html ":ignore") is a single HTML page with its images in `docs/slides/img/`.
GitHub only shows its source, so either download the PDF export or serve the HTML over HTTP and open it in a browser.

## PDF export

Every [GitHub release](https://github.com/B-AROL-O/agenthon-2026/releases) of this repository has a PDF of the deck attached, named `track2-pitch-deck-<tag>.pdf`.
The [Pitch deck PDF workflow](https://github.com/B-AROL-O/agenthon-2026/blob/main/.github/workflows/deck-pdf.yml) builds it with [`scripts/deck-to-pdf.sh`](https://github.com/B-AROL-O/agenthon-2026/blob/main/scripts/deck-to-pdf.sh).

## Serve the HTML deck

From a terminal at the root of the repository, for example inside the devcontainer in Visual Studio Code or GitHub Codespaces:

```bash
python3 -m http.server 8000 --directory docs/slides
```

Visual Studio Code forwards port 8000 automatically: click **Open in Browser** in the notification, or open the **Ports** panel and click the globe icon next to port 8000.
Then add `track2-pitch-deck.html` to the address, for example <http://localhost:8000/track2-pitch-deck.html>.
Stop the server with <kbd>Ctrl</kbd>+<kbd>C</kbd>.

## Keyboard controls

- <kbd>→</kbd>, <kbd>↓</kbd> or <kbd>Space</kbd>: next slide; <kbd>←</kbd> or <kbd>↑</kbd>: previous slide; <kbd>Home</kbd> and <kbd>End</kbd>: first and last slide
- <kbd>P</kbd>: presentation mode, one slide per screen without speaker notes; <kbd>F</kbd>: full screen; <kbd>Esc</kbd>: back to the scrolling view with notes
- Add `#N` to the address to open slide N, for example `track2-pitch-deck.html#5`

<!-- EOF -->
