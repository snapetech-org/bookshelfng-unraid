# Install BookshelfNG on Unraid

BookshelfNG is a Snapetech NG fork of Bookshelf for ebook and audiobook library
management and acquisition. It works independently; SeerrNG integration is optional.

> **Final release:** BookshelfNG `0.4.21.71` is published. The latest public ChaptarrNG release is `v0.9.977`; it accepts migration-158 SQLite and rejects older schemas. The unreleased older-schema SQLite and one-schema PostgreSQL candidate is in [ChaptarrNG PR #131](https://github.com/snapetech-org/chaptarrng/pull/131).
>
> Run [39131142836](https://github.com/snapetech-org/chaptarrng/actions/runs/39131142836) on code head `0f7a77d` failed in the PostgreSQL test fixture after reaching the migration and rollback assertions: its `ReadConfigValue` helper queried the mixed-case `Config` table without quotes, so PostgreSQL reported `relation "config" does not exist`. This identifies a fixture SQL error, not a converter assertion failure. Commit [ceef1797](https://github.com/snapetech-org/chaptarrng/commit/ceef1797) quotes the table name; exact-head run [39131508562](https://github.com/snapetech-org/chaptarrng/actions/runs/39131508562) is validating that fix. Do not use the candidate with operator data.
>
> BookshelfNG's fail-closed release gate merged to `main` as `c6b4642`; its readiness variable remains unset and the published `.71` release remains the final release. Populated-data migration, rollback, and the Community Apps upgrade flow remain unaccepted.

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
