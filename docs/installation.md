# Install BookshelfNG on Unraid

BookshelfNG is a Snapetech NG fork of Bookshelf for ebook and audiobook library
management and acquisition. It works independently; SeerrNG integration is optional.

> **Final release:** BookshelfNG `0.4.21.71` is published. The latest public ChaptarrNG release is `v0.9.977`; it accepts migration-158 SQLite and rejects older schemas. The unreleased older-schema SQLite and one-schema PostgreSQL candidate is in [ChaptarrNG PR #131](https://github.com/snapetech-org/chaptarrng/pull/131).
>
> ChaptarrNG PR #131 remains draft. Exact-head run [39196795646](https://github.com/snapetech-org/chaptarrng/actions/runs/39196795646) passed on head 2c0401fc: Linux, macOS, and Windows build/tests, PostgreSQL migration fixtures, release-note validation, CodeQL, dependency and secret checks, NuGet submission, and runner-receipt reconciliation. Disposable-fork validation was skipped by its gate. The preceding run [39195460843](https://github.com/snapetech-org/chaptarrng/actions/runs/39195460843) found four Windows fixtures that used POSIX-only paths; the native temporary-path fix passes.
>
> A copy-only populated migration rehearsal passed preview, apply, restore preview, and rollback with native Hardcover mode and network access disabled. The source copy remained unchanged, rollback restored the retained source backup byte-for-byte, and the converted database remained separate. This is one migration-158 SQLite candidate rehearsal, not cutover approval. Ambiguous media, older-schema and PostgreSQL operator-data acceptance, feature parity, installed rollback, and installation-channel acceptance remain open. The transition template's static preservation check passes, but the Community Apps upgrade flow has not been tested; keep PR #5 in draft.
>
> BookshelfNG PR #154's improved empty-file selection is on source `main`, not the published `.71` helper. The `.71` helper can print a zero-byte `readarr.db` beside a populated `audioarr.db`; ChaptarrNG `.977` resolves the populated file independently. The release gate remains closed, and populated-data migration, rollback, and the Community Apps upgrade flow remain unaccepted.

The ChaptarrNG handoff supports one database per appdata directory. If two
legacy database files are populated in the same directory, migration stops
without merging them. Migrate independent installations separately, or first
use BookshelfNG's
[two-instance media-consolidation runbook](https://github.com/snapetech-org/bookshelfng/blob/main/README.md#one-instance-for-ebooks-and-audiobooks)
to move and import tracked media into one BookshelfNG instance. The runbook
does not merge database histories, profiles, monitoring, or settings.

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
- Open the web interface on port 8787 and configure indexers and download clients.
- One instance can manage ebooks and audiobooks. SeerrNG can use two service
  entries with the same URL and API key when requesting both formats.
- Existing Readarr or softcover databases require migration before using the
  Hardcover image; changing the image tag alone is not a migration.

## Source and support

- [BookshelfNG application source and documentation](https://github.com/snapetech-org/bookshelfng)
- [Unraid package and SeerrNG integration support](https://github.com/snapetech-org/seerrng/issues)

BookshelfNG is derived from Bookshelf and Readarr and distributed under GPLv3.
