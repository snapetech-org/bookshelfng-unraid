# Install BookshelfNG on Unraid

BookshelfNG is a Snapetech NG fork of Bookshelf for ebook and audiobook library
management and acquisition. It works independently; SeerrNG integration is optional.

> **Latest published releases:** BookshelfNG `0.4.21.71` and ChaptarrNG `v0.9.977`. The published ChaptarrNG migration supports migration-158 SQLite; older schemas and PostgreSQL sources are unsupported by that release.
>
> ChaptarrNG PR #131 remains open and draft. Its latest application-code snapshot is `38be9422a0390c0b3d4d1c453ec14b25d3aa99a4`; the current documentation-only PR head is `73fbc716974ba0dcdb8104f0c5d6a8115fec2feb`. Exact-head Build [39267876585](https://github.com/snapetech-org/chaptarrng/actions/runs/39267876585) passed Linux, macOS, Windows, PostgreSQL migration, release-note, and native-runner receipt checks. CodeQL [118112421054](https://github.com/snapetech-org/chaptarrng/runs/118112421054), security analysis [39267876503](https://github.com/snapetech-org/chaptarrng/actions/runs/39267876503), and dependency review [39267876754](https://github.com/snapetech-org/chaptarrng/actions/runs/39267876754) passed; disposable-fork validation was skipped by its external-fork gate. The current PR head adds documentation only; these checks do not establish operator-data or installation acceptance. The Unraid transition [PR #5](https://github.com/snapetech-org/bookshelfng-unraid/pull/5) remains draft; its template-preservation script passes locally, but GitHub reports no PR checks and the real Community Applications upgrade and rollback flow has not been accepted. Keep the release freeze: representative-data, parity, installed-rollback, and update-channel acceptance remain open. Do not point ChaptarrNG at live BookshelfNG appdata or use the candidate restore flow for production migration.
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
`ghcr.io/snapetech-org/bookshelfng:latest`. Stable releases keep `:main`,
`:master`, and `:latest` on the same image; branch builds use development tags.

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
