# Install BookshelfNG on Unraid

BookshelfNG is a Snapetech NG fork of Bookshelf for ebook and audiobook library
management and acquisition. It works independently; SeerrNG integration is optional.

> **Published state:** BookshelfNG `0.4.21.71` and ChaptarrNG `v0.9.977` remain the latest releases. The published converter is preview-only for migration-158 SQLite. While [BookshelfNG issue #144](https://github.com/snapetech-org/bookshelfng/issues/144) remains open, do not apply migration or start ChaptarrNG against BookshelfNG appdata.
>
> Current candidate status (2026-10-19): ChaptarrNG PR #131 is at code head
> `a6d7908e937c870a4b2d3209f5aafbb9b640f6cd`. Exact-head Build
> [39357519729](https://github.com/snapetech-org/chaptarrng/actions/runs/39357519729) is queued; the previous code head
> `e4b909ff` is under hosted validation in Build
> [39357406142](https://github.com/snapetech-org/chaptarrng/actions/runs/39357406142). On code head `969fb20b`, Build [39353846035](https://github.com/snapetech-org/chaptarrng/actions/runs/39353846035) first stopped on HTTP 403 while
> downloading the pinned BookshelfNG `.71` archive; retrying that old code then
> failed when raw WAL fingerprinting read `readarr.db-wal` while the SQLite
> guard held it open. Rollback also left the service marked for deletion while
> a PowerShell `ServiceController` handle remained open. Commit `e4b909ff` adds
> archive retry/backoff and captures raw fingerprints outside the guard lifetime;
> commit `a6d7908e` disposes the service handle before waiting for removal. The
> exact Linux artifact from `969fb20b` passed the populated migration and
> SeerrNG lifecycle smokes with synthetic records. PR #131 remains draft and
> unpublished. No release, package, image, or bridge was published.
> Representative operator data, exhaustive semantic disposition, provider
> fulfillment, installation-channel handoff, and operator acceptance remain open.
> Keep BookshelfNG in service; do not apply production migration.
>
> The Unraid transition [PR #5](https://github.com/snapetech-org/bookshelfng-unraid/pull/5) remains draft. Its hosted template-preservation check passed in [run 39340676919](https://github.com/snapetech-org/bookshelfng-unraid/actions/runs/39340676919). That check validates the candidate XML and settings preservation; it does not exercise a live Community Applications update or rollback. Both release-readiness gates remain unset; no migration bridge is published.

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
`ghcr.io/snapetech-org/bookshelfng:latest`. Stable releases keep `:main`,
`:master`, and `:latest` on the same image; branch builds use development tags.

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
