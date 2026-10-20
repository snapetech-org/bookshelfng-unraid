# BookshelfNG for Unraid

This repository publishes the standalone BookshelfNG Unraid Docker template.
**Built on .NET 10 LTS**, BookshelfNG is a Snapetech NG fork of Bookshelf for
ebook and audiobook library management and acquisition. It works independently;
SeerrNG integration is optional.

> **Published state:** BookshelfNG `0.4.21.71` and ChaptarrNG `v0.9.977` remain the latest releases. The published converter is preview-only for migration-158 SQLite. While [BookshelfNG issue #144](https://github.com/snapetech-org/bookshelfng/issues/144) remains open, do not apply migration or start ChaptarrNG against BookshelfNG appdata.
>
> **ChaptarrNG migration candidate:** PR #131 remains draft at code head
> `1a1c7320530c4c17184b35a727ef9d14ccbcd8ec`. At the 2026-10-20 04:38 UTC
> status check, exact-head Build [39370145050](https://github.com/snapetech-org/chaptarrng/actions/runs/39370145050)
> had its macOS and Windows jobs in progress; Linux, PostgreSQL migration, and
> release-note contract were queued. CodeQL [39370141179](https://github.com/snapetech-org/chaptarrng/actions/runs/39370141179),
> Security Analysis [39370145142](https://github.com/snapetech-org/chaptarrng/actions/runs/39370145142),
> dependency review [39370145010](https://github.com/snapetech-org/chaptarrng/actions/runs/39370145010),
> Helm validation [39370145008](https://github.com/snapetech-org/chaptarrng/actions/runs/39370145008),
> and NuGet submission [39370138436](https://github.com/snapetech-org/chaptarrng/actions/runs/39370138436)
> were queued. Trivy [39370145017](https://github.com/snapetech-org/chaptarrng/actions/runs/39370145017)
> and Semgrep [39370145016](https://github.com/snapetech-org/chaptarrng/actions/runs/39370145016)
> were pending. Earlier exact-head candidate `7ff38a58` passed Linux, macOS,
> Windows, PostgreSQL migration, receipt reconciliation, CodeQL, security,
> Trivy, dependency review, and NuGet checks. The intermediate merge candidate
> `3f54017d` exposed a macOS validation failure because its receipt used SDK
> 10.0.401 while the validation task required 10.0.402. Candidate `1a1c7320`
> aligns global.json and Docker SDK images to .NET 10.0.402; its exact-head
> validation is running. Representative data, semantic feature parity, provider
> fulfillment, installed rollback, update-channel handoff, and operator
> acceptance remain open. Keep BookshelfNG in service; no release, package,
> image, or migration bridge is authorized.
>
> The Unraid transition [PR #5](https://github.com/snapetech-org/bookshelfng-unraid/pull/5)
> remains draft. The latest template-preservation check [39358120264](https://github.com/snapetech-org/bookshelfng-unraid/actions/runs/39358120264)
> passed at code head `434138d5`; it validates XML and preserved settings only.
> The live Community Applications upgrade and rollback have not been exercised,
> and `templates/bookshelfng.xml` on `main` still installs BookshelfNG.

## Existing installations

Keep the current BookshelfNG image. The cutover is frozen: read-only preview is
allowed, but do not apply migration or switch an existing appdata directory to
ChaptarrNG while BookshelfNG issue #144 remains open. The legacy Community Apps
template on `main` still points to BookshelfNG. A transition
candidate keeps the existing BookshelfNG entry, appdata path, port, media and
download mappings, user IDs, timezone, and Hardcover settings while switching
to the standard ChaptarrNG image. It is not published and must remain on its
feature branch until the application release and Unraid update-flow gates
pass. The XML and settings-preservation check passed; run
`python3 scripts/test-transition-template.py` to repeat it. Read the
[BookshelfNG-to-ChaptarrNG migration guide](https://github.com/snapetech-org/bookshelfng/blob/main/docs/migrate-from-bookshelfng-to-chaptarrng.md).
When cutover is approved, upgrade BookshelfNG to `.71`, stop the service, and
keep an independent appdata backup before switching. New installations should use the
[ChaptarrNG Unraid template](https://github.com/snapetech-org/chaptarrng-unraid).
For a manual BookshelfNG install needed to inspect or roll back an existing
library, use [the legacy template XML](templates/bookshelfng.xml); it installs
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
This template repository uses the same GPLv3 license.

## Security scanning

Run [`scripts/security-scan-local.sh`](scripts/security-scan-local.sh) for local
Semgrep Community Edition and applicable Trivy scans. The public GitHub Actions
workflows run these scans on changes and weekly, alongside the existing CodeQL
workflow. See [security-scanning.md](docs/security-scanning.md) for offline
setup and updates. Run [`scripts/install-security-hooks.sh`](scripts/install-security-hooks.sh)
once to enable the staged Semgrep pre-commit hook.
