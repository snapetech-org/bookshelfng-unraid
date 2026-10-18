# BookshelfNG legacy template for Unraid

This repository keeps the existing BookshelfNG Unraid template while preparing
its handoff to ChaptarrNG. The final BookshelfNG source release is `0.4.21.71`.

> The transition template points at `ghcr.io/snapetech-org/chaptarrng:latest` and
> keeps the existing `/config`, `/data`, `/download`, port 8787, PUID/PGID, TZ,
> and Hardcover settings. Do not publish or apply it while ChaptarrNG's
> retirement release freeze is active. Public `v0.9.977` accepts migration-158
> SQLite; upgrade BookshelfNG to `.71` first. The version-aware older-schema
> fix is merged to ChaptarrNG `main` but is not in a public release.

## Existing installations

Use the [BookshelfNG-to-ChaptarrNG migration guide](https://github.com/snapetech-org/bookshelfng/blob/main/docs/migrate-from-bookshelfng-to-chaptarrng.md).
Stop BookshelfNG, back up the complete appdata directory, and keep the same
media and download mounts. ChaptarrNG migrates the database on startup and
retains a BookshelfNG backup. The final BookshelfNG `.71` image can bring older
schemas to migration 158 before switching; ChaptarrNG `.977` rejects versions
before migration 14. PR #126 merged the version-aware fix to ChaptarrNG `main`,
but the fix is unpublished while the release freeze is active. PostgreSQL
sources and two populated BookshelfNG databases are not supported.

ChaptarrNG PR #129 merged the M4B compatibility source and PR #130 merged a
lossy mapping from BookshelfNG's 50–99 import threshold to ChaptarrNG's
matching modes. Neither change is in public `.977`; keep
`BOOKSHELF_M4B_MERGE` unset. The matching modes use different algorithms, so
the mapping still needs converted-library acceptance.

An isolated Docker image-switch rehearsal used the published `.71` and `.977`
images with an empty migration-158 database. Startup conversion, source backup,
rollback, and a subsequent BookshelfNG start on port 8787 passed. This does not
validate populated operator data or the Community Apps template update flow.
Keep an independent backup until the converted library and external clients
have been checked.

New installations should use the
[ChaptarrNG Unraid template](https://github.com/snapetech-org/chaptarrng-unraid).
