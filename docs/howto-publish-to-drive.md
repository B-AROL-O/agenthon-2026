# HOWTO Publish the Track 2 deliverables to Google Drive

<!-- (2026-11-21) -->

[`scripts/publish-to-drive.sh`](https://github.com/B-AROL-O/agenthon-2026/blob/main/scripts/publish-to-drive.sh) copies the deliverables into the [submission Drive folder](https://drive.google.com/drive/folders/1mL-yWZ0gsObf_6VHV3TmJgGfv0_Wswkp).
Each owner publishes their own part from the machine that has the files:

| Part     | Drive folders                                 | Owner   | Local source                                               |
| -------- | --------------------------------------------- | ------- | ---------------------------------------------------------- |
| `spot`   | `01-spot/`                                    | Luca    | Any folder with the final exports, given with `--spot-dir` |
| `static` | `02-social/`, `03-web-print/`, `04-ad-image/` | Alessio | `genai/out/drive/`, written by `uv run campaign.py`        |
| `docs`   | `05-project-sheet/`, `06-tools-list/`         | Anyone  | `docs/track2-project-sheet.md` and `docs/track2-tools.md`  |

The script never deletes anything in Drive: it only adds new files and updates changed ones.
Without `--run` it is a dry run that only lists what it would upload.

## Deadline guard

The team freezes the submission folder at **16:45** (see the [timeline and WBS](track2-wbs.md)), and the final review runs from 16:15 to 16:30, so publish before 16:15.
After 16:45 the script refuses to upload, unless you pass `--force-late` for an emergency fix the team agreed on.
After 16:59 it always refuses: Drive records the file timestamps at **17:00**, and a file changed after that no longer counts.

## One-time setup

You need edit access to the submission folder with your own Google account.

1. Install rclone.
   In the devcontainer it is already installed (rebuild the container if `rclone version` fails).
   On Arch Linux: `sudo pacman -S rclone`; on macOS: `brew install rclone`; elsewhere see <https://rclone.org/install/>.
2. Run `rclone config` and answer:
   - `n` for a new remote, name it `gdrive`
   - Storage: `drive` (Google Drive)
   - `client_id` and `client_secret`: press Enter to leave them empty
   - Scope: `1` (full access; needed to see a folder shared with you)
   - `service_account_file`: press Enter; advanced config: `n`
   - Use a web browser to authenticate: `y`, then open the link it prints and sign in.
     In the devcontainer, VS Code forwards port 53682, so the link opens in your normal browser.
     If that fails, answer `n` instead and run `rclone authorize "drive"` on a machine with a browser, then paste the token back.
   - Shared drive: `n`; then `y` to keep the remote
3. Check it can see the folder:
   `rclone lsd gdrive: --drive-root-folder-id 1mL-yWZ0gsObf_6VHV3TmJgGfv0_Wswkp`

## Publish

```bash
# Dry run first: shows what would be uploaded
scripts/publish-to-drive.sh docs

# Then publish for real
scripts/publish-to-drive.sh --run docs

# Alessio, after `cd genai && uv run campaign.py`
scripts/publish-to-drive.sh --run static

# Luca, from the folder with the final spot exports
scripts/publish-to-drive.sh --run --spot-dir ~/spot/final spot
```

`docs` renders each Markdown file twice, with Docker and the [publish-md-pdf](https://github.com/B-AROL-O/publish-md-pdf) image:

- an A4 PDF;
- a DOCX that Drive imports as an editable Google Doc.

The first run pulls the image, which takes a few minutes, so run it once before the freeze.

After a real upload, set the deliverable's status to **In Drive** in the Track 2 deliverables index.

Settings can be overridden with the `DRIVE_REMOTE` (default `gdrive:`) and `DRIVE_FOLDER_ID` environment variables.

<!-- EOF -->
