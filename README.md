# BookshelfNG for Unraid

This repository publishes the standalone BookshelfNG Unraid Docker template.
**Built on .NET 10 LTS**, BookshelfNG is a Snapetech NG fork of Bookshelf for
ebook and audiobook library management and acquisition. It works independently;
SeerrNG integration is optional.

> **Published state:** BookshelfNG `0.4.21.71` and ChaptarrNG `v0.9.977` remain the latest releases. The published converter is preview-only for migration-158 SQLite. While [BookshelfNG issue #144](https://github.com/snapetech-org/bookshelfng/issues/144) remains open, do not apply migration or start ChaptarrNG against BookshelfNG appdata.
>
> **ChaptarrNG migration candidate:** PR #131 remains draft at code head
> `730ba5e85d480a71aab52f0cae8541e40b57811b`. At the 2026-10-20 04:50 UTC
> check, Windows in exact-head Build [39371469467](https://github.com/snapetech-org/chaptarrng/actions/runs/39371469467)
> was in progress; Linux, macOS, PostgreSQL migration, and the release-note
> contract were queued. CodeQL [39371467266](https://github.com/snapetech-org/chaptarrng/actions/runs/39371467266),
> Security Analysis [39371469595](https://github.com/snapetech-org/chaptarrng/actions/runs/39371469595),
> dependency review [39371469626](https://github.com/snapetech-org/chaptarrng/actions/runs/39371469626),
> Helm validation [39371469558](https://github.com/snapetech-org/chaptarrng/actions/runs/39371469558),
> and NuGet submission [39371468020](https://github.com/snapetech-org/chaptarrng/actions/runs/39371468020)
> were queued. Trivy [39371469459](https://github.com/snapetech-org/chaptarrng/actions/runs/39371469459)
> and Semgrep [39371469456](https://github.com/snapetech-org/chaptarrng/actions/runs/39371469456)
> were pending. Earlier exact-head candidate `7ff38a58` passed Linux, macOS,
> Windows, PostgreSQL migration, receipt reconciliation, CodeQL, security,
> Trivy, dependency review, and NuGet checks. Candidate `3f54017d` exposed the
> .NET SDK mismatch that caused its macOS validation tests to be skipped.
> Candidate `1a1c7320` aligned the global pin, three primary Docker build images,
> and hosted workflow pins, but missed `integration/Dockerfile.m4b-test`.
> Candidate `730ba5e8` updates that fourth image and adds a guard that checks all
> Docker and hosted SDK pins against `global.json`. Representative data, semantic
> parity, installed rollback, provider fulfillment, update-channel handoff, and
> operator acceptance remain open. Keep BookshelfNG running; no release, package,
> image, or migration bridge is authorized.
>
> **Unraid transition:** [PR #5](https://github.com/snapetech-org/bookshelfng-unraid/pull/5)
> remains draft at current documentation head
> `697ae718ada609d2fdb0a91fd43e381d71d02f48`. The last template-preservation
> check [39358120264](https://github.com/snapetech-org/bookshelfng-unraid/actions/runs/39358120264)
> passed on code head `434138d5654c7b284b92e411423f919b13a32b3e`; the later
> documentation-only commit leaves the template unchanged. This check covers
> XML and preserved settings only. A live Community Applications upgrade and
> rollback have not been exercised. The template on `main` still installs
> BookshelfNG.


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
This template repository uses the same GPLv3 license.


## Security scanning

Run [`scripts/security-scan-local.sh`](scripts/security-scan-local.sh) for local
Semgrep Community Edition and applicable Trivy scans. The public GitHub Actions
workflows run these scans on changes and weekly, alongside CodeQL. See
[security-scanning.md](docs/security-scanning.md) for offline setup and updates.
Run [`scripts/install-security-hooks.sh`](scripts/install-security-hooks.sh) once
to enable the staged Semgrep pre-commit hook.
