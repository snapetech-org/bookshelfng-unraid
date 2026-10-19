# Install BookshelfNG on Unraid

BookshelfNG is a Snapetech NG fork of Bookshelf for ebook and audiobook library
management and acquisition. It works independently; SeerrNG integration is optional.

> **Final releases:** BookshelfNG `0.4.21.71` and ChaptarrNG `v0.9.977` remain the latest public releases. Published ChaptarrNG supports migration-158 SQLite and rejects older schemas; it does not support PostgreSQL source conversion. The unreleased older-SQLite and one-schema PostgreSQL candidate remains in draft [ChaptarrNG PR #131](https://github.com/snapetech-org/chaptarrng/pull/131).
>
> Candidate code snapshot `8b4c6e23` passed exact-head Build run [39205452341](https://github.com/snapetech-org/chaptarrng/actions/runs/39205452341), including Linux, macOS, Windows, PostgreSQL migration fixtures, release-note validation, and native-runner receipt reconciliation. CodeQL [39205449712](https://github.com/snapetech-org/chaptarrng/actions/runs/39205449712), dependency review [39205452346](https://github.com/snapetech-org/chaptarrng/actions/runs/39205452346), security scan [39205452337](https://github.com/snapetech-org/chaptarrng/actions/runs/39205452337), and NuGet submission [39205449409](https://github.com/snapetech-org/chaptarrng/actions/runs/39205449409) also passed. These are candidate checks, not approval to migrate an installation.
>
> BookshelfNG's fail-closed release gate merged to `main` as `c6b4642`; its readiness variable remains unset. One disposable populated SQLite copy passed preview, apply, restore preview, and rollback. Representative operator-data validation and the actual Community Apps upgrade and rollback flow remain unaccepted. No release or compatibility bridge is published.

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
