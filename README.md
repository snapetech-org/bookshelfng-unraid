# BookshelfNG for Unraid

This repository publishes the standalone BookshelfNG Unraid Docker template.
**Built on .NET 10 LTS**, BookshelfNG is a Snapetech NG fork of Bookshelf for
ebook and audiobook library management and acquisition. It works independently;
SeerrNG integration is optional.

> **Latest published releases:** BookshelfNG `0.4.21.71` and ChaptarrNG `v0.9.977`. The published ChaptarrNG migration supports migration-158 SQLite; older schemas and PostgreSQL sources are unsupported by that release.
>
> ChaptarrNG [PR #131](https://github.com/snapetech-org/chaptarrng/pull/131) remains a draft. Its candidate adds older SQLite migrations, one PostgreSQL source schema, explicit Hardcover identity handling, BookOrbit, media moves, and BookshelfNG ZIP-backup restore. Candidate validation, representative-data migration and rollback, feature-parity review, and update-channel acceptance remain open. Do not point ChaptarrNG at live BookshelfNG appdata.
>
> A copy-only populated migration-158 SQLite rehearsal passed preview, apply, restore preview, and rollback with native Hardcover mode and networking disabled. It retained the source backup and restored that backup byte-for-byte. This was one rehearsal and does not establish operator-data acceptance. The candidate restore change is not in public `.977`.
>
> The published `.977` maps bare numeric provider IDs to Goodreads regardless of `HARDCOVER`; do not use it with native Hardcover BookshelfNG data. The candidate requires an explicit source mode. Preserve `HARDCOVER=false` for Goodreads-primary installations.
>
> The published `.71` helper can see a zero-byte `readarr.db` beside a populated `audioarr.db`; source PR #154 fixes that selection but is not in `.71`. ChaptarrNG handles one source database per appdata directory and does not merge databases, histories, profiles, monitoring, or settings.
>
> The Unraid transition [PR #5](https://github.com/snapetech-org/bookshelfng-unraid/pull/5) remains a draft. The template-preservation check passes, but the real Community Applications upgrade and rollback flow has not been accepted. Both release-readiness gates remain unset; no migration bridge is published.

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
