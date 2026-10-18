# Install BookshelfNG on Unraid

BookshelfNG is a Snapetech NG fork of Bookshelf for ebook and audiobook library
management and acquisition. It works independently; SeerrNG integration is optional.

> **Final release:** BookshelfNG `0.4.21.71` is the final source release. The
> legacy template on `main` has not yet moved to ChaptarrNG. The latest
> published ChaptarrNG release is `v0.9.977`, which accepts migration-158
> SQLite and rejects older source schemas. An unreleased older-schema SQLite
> upgrade path and one-schema PostgreSQL converter are under review in
> [ChaptarrNG PR #131](https://github.com/snapetech-org/chaptarrng/pull/131);
> The `e67f28ed` run found a staging-schema column bug; `8f0bbc29` fixed it,
but its hosted build then failed because the runner API did not expose
`VersionLoader`. Commit `50f58223` reads the registered
`IVersionTableMetaData` service, and exact-head CI is running.
> BookshelfNG's fail-closed publishing gate is under review in
> [PR #148](https://github.com/snapetech-org/bookshelfng/pull/148). No new
> release or image will be published while operator-data migration, rollback,
> and installer acceptance remain open. An empty-database Docker image-switch
> and rollback smoke passed; populated data and the Community Apps template
> update remain untested.

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
