# BookshelfNG for Unraid

This repository publishes the standalone BookshelfNG Unraid Docker template.
**Built on .NET 10 LTS**, BookshelfNG is a Snapetech NG fork of Bookshelf for
ebook and audiobook library management and acquisition. It works independently;
SeerrNG integration is optional.

> **Final release:** BookshelfNG `0.4.21.71` is published. The latest public ChaptarrNG release is `v0.9.977`; it accepts migration-158 SQLite and rejects older schemas. The unreleased older-schema SQLite and one-schema PostgreSQL candidate is in [ChaptarrNG PR #131](https://github.com/snapetech-org/chaptarrng/pull/131).
>
> Earlier exact-head ChaptarrNG PR #131 run [39152023939](https://github.com/snapetech-org/chaptarrng/actions/runs/39152023939) on `ea6fcd46` passed Linux, macOS, and Windows builds and test suites, PostgreSQL migrations, release-note validation, native-runner receipt reconciliation, CodeQL, dependency review, and security checks. Windows reported 4,349 tests passed and none failed. These are candidate CI checks only; the candidate remains unsupported for operator data.
>
> BookshelfNG PR #154's improved empty-file selection is on source `main`, not the published `.71` helper. The `.71` helper can print a zero-byte `readarr.db` beside a populated `audioarr.db`; ChaptarrNG `.977` resolves the populated file independently. The release gate remains closed, and populated-data migration, rollback, and the Community Apps upgrade flow remain unaccepted.
>
> Follow-up populated image-switch evidence (2026-10-18): the prior ChaptarrNG candidate mapped bare numeric Hardcover IDs as Goodreads when the source's `HARDCOVER=true` was dropped. Repeating with the same mode preserved Hardcover IDs and API results; rollback restored the source database byte-for-byte and the published `.71` image reopened it. ChaptarrNG PR #131 head [`4fff834d`](https://github.com/snapetech-org/chaptarrng/commit/4fff834d6c4f8e9fd03b712a5e2b02639a53c76a) now fails closed without an explicit mode and adds separate compatibility image targets. Exact-head hosted CI is still running; this remains synthetic evidence, not operator-data or Community Apps acceptance. Keep this PR in draft and leave the release gate closed.

The ChaptarrNG handoff supports one database per appdata directory. Two
populated legacy database files stop migration rather than being selected or
merged. Keep independent installations separate, or use BookshelfNG's
[two-instance media-consolidation runbook](https://github.com/snapetech-org/bookshelfng/blob/main/README.md#one-instance-for-ebooks-and-audiobooks)
to move and import tracked media into one BookshelfNG instance before migrating
that instance. Database histories, profiles, monitoring, and settings are not
merged.

## Existing installations

Keep the current BookshelfNG image until you are ready to migrate. The legacy
Community Apps template on `main` still points to BookshelfNG. A transition
candidate keeps the existing BookshelfNG entry, appdata path, port, media and
download mappings, user IDs, timezone, and Hardcover settings while switching
to the standard ChaptarrNG image. It is not published and must remain on its
feature branch until the application release and Unraid update-flow gates
pass. The XML and settings-preservation check passed; run
`python3 scripts/test-transition-template.py` to repeat it. Read the
[BookshelfNG-to-ChaptarrNG migration guide](https://github.com/snapetech-org/bookshelfng/blob/main/docs/migrate-from-bookshelfng-to-chaptarrng.md),
upgrade BookshelfNG to `.71`, stop the service, and keep an independent
appdata backup before switching. New installations should use the
[ChaptarrNG Unraid template](https://github.com/snapetech-org/chaptarrng-unraid).
For a manual BookshelfNG install needed to inspect or roll back an existing
library, use [the legacy template XML](templates/bookshelfng.xml); it installs
`ghcr.io/snapetech-org/bookshelfng:main`.

- Map persistent appdata to `/config` and your media to `/data`.
- Map downloads to `/download`, matching your download client's container paths.
- Set a personal Hardcover API token in `HARDCOVER_AUTH` or BookshelfNG settings.
- Preserve the existing `HARDCOVER` mode during conversion. This template
  keeps native Hardcover mode enabled by default; Goodreads-primary databases
  must retain `HARDCOVER=false` so their bare numeric IDs are not reclassified.
- Open the web interface on port 8787 and configure indexers and download clients.
- One instance can manage ebooks and audiobooks. SeerrNG can use two service
  entries with the same URL and API key when requesting both formats.
- Existing Readarr or softcover databases require migration before using the
  Hardcover image; changing the image tag alone is not a migration.

## Source and support

- [BookshelfNG application source and documentation](https://github.com/snapetech-org/bookshelfng)
- [Unraid package and SeerrNG integration support](https://github.com/snapetech-org/seerrng/issues)

BookshelfNG is derived from Bookshelf and Readarr and distributed under GPLv3.
This template repository uses the same GPLv3 license.
