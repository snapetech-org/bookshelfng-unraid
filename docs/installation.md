# Install BookshelfNG on Unraid

BookshelfNG is a Snapetech NG fork of Bookshelf for ebook and audiobook library
management and acquisition. It works independently; SeerrNG integration is optional.

> **Final releases:** BookshelfNG `0.4.21.71` and ChaptarrNG `v0.9.977` remain the latest public releases. Published ChaptarrNG supports migration-158 SQLite and rejects older schemas; it does not support PostgreSQL source conversion. The unreleased older-SQLite and one-schema PostgreSQL candidate remains in draft [ChaptarrNG PR #131](https://github.com/snapetech-org/chaptarrng/pull/131).
>
> Candidate ChaptarrNG code snapshot `8b4c6e23` passed exact-head Build run [39205452341](https://github.com/snapetech-org/chaptarrng/actions/runs/39205452341), including Linux, macOS, Windows, PostgreSQL migration, release-note, and runner-receipt checks. CodeQL [39205449712](https://github.com/snapetech-org/chaptarrng/actions/runs/39205449712), dependency review [39205452346](https://github.com/snapetech-org/chaptarrng/actions/runs/39205452346), security scan [39205452337](https://github.com/snapetech-org/chaptarrng/actions/runs/39205452337), and NuGet submission [39205449409](https://github.com/snapetech-org/chaptarrng/actions/runs/39205449409) also passed. Current docs-only PR #131 head `f76aeb9e` passed cross-platform Build [39207407047](https://github.com/snapetech-org/chaptarrng/actions/runs/39207407047), CodeQL [39207403913](https://github.com/snapetech-org/chaptarrng/actions/runs/39207403913), security scan [39207407043](https://github.com/snapetech-org/chaptarrng/actions/runs/39207407043), dependency review [39207407105](https://github.com/snapetech-org/chaptarrng/actions/runs/39207407105), NuGet submission [39207406945](https://github.com/snapetech-org/chaptarrng/actions/runs/39207406945), and release-note revalidation [39209201999](https://github.com/snapetech-org/chaptarrng/actions/runs/39209201999). These checks do not approve migration to operator data.
>
> One copy-only populated migration rehearsal passed preview, apply, restore preview, and rollback with native Hardcover mode and networking disabled. Preview left the source copy unchanged; rollback restored the retained backup byte-for-byte and kept the converted database separately. This is one migration-158 SQLite rehearsal, not operator-data or cutover approval. Ambiguous media, older SQLite and PostgreSQL operator data, feature disposition, installed rollback, and channel acceptance remain open.
>
> BookshelfNG PR #154's improved empty-file selection is on source `main`, not the published `.71` helper. The `.71` helper can report a zero-byte `readarr.db` beside a populated `audioarr.db`; ChaptarrNG `.977` independently chooses the populated database.
>
> The handoff keeps the source provider mode for bare numeric IDs. The legacy template defaults `HARDCOVER=true`; Goodreads-primary installs must preserve `HARDCOVER=false`. Missing mode fails closed when numeric IDs are present.
>
> The transition template's static preservation test passes, but the Community Apps upgrade and rollback flow has not been tested. Keep Unraid PR #5 in draft. No release, package, image, listing, or compatibility bridge is published.
>
> The ChaptarrNG handoff supports one database per appdata directory. Two populated legacy databases in one directory stop migration instead of being merged. Keep independent installations separate, or use BookshelfNG's [two-instance media-consolidation runbook](https://github.com/snapetech-org/bookshelfng/blob/main/README.md#one-instance-for-ebooks-and-audiobooks) to move tracked media into one BookshelfNG instance first. Database histories, profiles, monitoring, and settings are not merged.

## Existing installations

Keep the current BookshelfNG image until you are ready to migrate. The legacy
Community Apps template on `main` still points to BookshelfNG. A transition
candidate preserves its appdata path, port, media/download mappings, user IDs,
timezone, and Hardcover settings while switching to the standard ChaptarrNG
image. It is not published and must remain on its feature branch until the
application release and Unraid update-flow gates pass. The XML and
settings-preservation check passed; run
`python3 scripts/test-transition-template.py` to repeat it.
Read the
[BookshelfNG-to-ChaptarrNG migration guide](https://github.com/snapetech-org/bookshelfng/blob/main/docs/migrate-from-bookshelfng-to-chaptarrng.md),
upgrade BookshelfNG to `.71`, stop the service, and keep an independent
appdata backup before switching. New installations should use the
[ChaptarrNG Unraid template](https://github.com/snapetech-org/chaptarrng-unraid).
For a manual BookshelfNG install needed to inspect or roll back an existing
library, use [the legacy template XML](../templates/bookshelfng.xml); it installs
`ghcr.io/snapetech-org/bookshelfng:main`.

- Map persistent appdata to `/config` and your media to `/data`.
- Map downloads to `/download`, matching your download client's container paths.
- Set a personal Hardcover API token in `HARDCOVER_AUTH` or BookshelfNG settings.
- Preserve the existing `HARDCOVER` mode. The template defaults to native
  Hardcover; Goodreads-primary databases must keep `HARDCOVER=false` so numeric
  provider IDs retain their meaning.
- Open the web interface on port 8787 and configure indexers and download clients.
- One instance can manage ebooks and audiobooks. SeerrNG can use two service
  entries with the same URL and API key when requesting both formats.
- Existing Readarr or softcover databases require migration before using the
  Hardcover image; changing the image tag alone is not a migration.

## Source and support

- [BookshelfNG application source and documentation](https://github.com/snapetech-org/bookshelfng)
- [Unraid package and SeerrNG integration support](https://github.com/snapetech-org/seerrng/issues)

BookshelfNG is derived from Bookshelf and Readarr and distributed under GPLv3.
