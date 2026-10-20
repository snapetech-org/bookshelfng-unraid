# Install BookshelfNG on Unraid

BookshelfNG is a Snapetech NG fork of Bookshelf for ebook and audiobook library
management and acquisition. It works independently; SeerrNG integration is optional.

> **Published state:** BookshelfNG `0.4.21.71` and ChaptarrNG `v0.9.977` remain the latest releases. The published converter is preview-only for migration-158 SQLite. While [BookshelfNG issue #144](https://github.com/snapetech-org/bookshelfng/issues/144) remains open, do not apply migration or start ChaptarrNG against BookshelfNG appdata.
>
> ChaptarrNG PR #131 merged on 2026-10-20 as
> `d2bcba7953a14d2d726f47005a660314cc5e4c26`, from code head
> `87c57a2bffd25a5ecbda40b9c63fd6d82993c54d`. Exact-head Build
> [39374140961](https://github.com/snapetech-org/chaptarrng/actions/runs/39374140961)
> passed Linux, macOS, Windows, PostgreSQL migration, release-note, and
> native-runner receipt checks. CodeQL, security analysis, Trivy, Semgrep
> Community, dependency review, NuGet, and Helm checks passed. Disposable-fork
> validation was skipped by its gate. The separate GHAS Semgrep OSS check failed
> with 12 SQL-format findings and three fixture-path warnings; those findings
> were reviewed and are not reported as a clean check. This is source and
> synthetic validation only. Representative data, feature parity, installed
> rollback, and installer/update-channel acceptance remain open. No release,
> package, image, or migration bridge was published. Keep BookshelfNG running.
>
> The Unraid transition [PR #5](https://github.com/snapetech-org/bookshelfng-unraid/pull/5)
> remains draft at branch head `6ae104976df445f8def9dabae6f10c3cda2c92d4`. Its latest
> template-preservation check
> [39358120264](https://github.com/snapetech-org/bookshelfng-unraid/actions/runs/39358120264)
> passed on code head `434138d5654c7b284b92e411423f919b13a32b3e`; later branch
> commits only refresh documentation. The check validates XML and preserved
> settings, not a live Community Applications update or rollback. The template
> on `main` still installs BookshelfNG. Both release-readiness gates remain
> unset; do not publish or apply the handoff.

## Existing installations

Keep the current BookshelfNG image. The cutover is frozen: read-only preview is
allowed, but do not apply migration or switch an existing appdata directory to
ChaptarrNG while BookshelfNG issue #144 remains open. The legacy Community Apps
template on `main` still points to BookshelfNG. A transition
candidate preserves its appdata path, port, media/download mappings, user IDs,
timezone, and Hardcover settings while switching to the standard ChaptarrNG
image. It is not published and must remain on its feature branch until the
application release and Unraid update-flow gates pass. The XML and
settings-preservation check passed; run
`python3 scripts/test-transition-template.py` to repeat it.
Read the
[BookshelfNG-to-ChaptarrNG migration guide](https://github.com/snapetech-org/bookshelfng/blob/main/docs/migrate-from-bookshelfng-to-chaptarrng.md).
When cutover is approved, upgrade BookshelfNG to `.71`, stop the service, and
keep an independent appdata backup before switching. New installations should use the
[ChaptarrNG Unraid template](https://github.com/snapetech-org/chaptarrng-unraid).
For a manual BookshelfNG install needed to inspect or roll back an existing
library, use [the legacy template XML](../templates/bookshelfng.xml); it installs
`ghcr.io/snapetech-org/bookshelfng:latest`. Stable releases keep `:stable`,
`:main`, `:master`, and `:latest` on the same verified image digest; branch
builds use development tags.

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
