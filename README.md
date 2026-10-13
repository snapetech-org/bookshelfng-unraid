# BookshelfNG legacy template for Unraid

This repository keeps the existing BookshelfNG Unraid template while preparing
its handoff to ChaptarrNG. The final BookshelfNG source release is `0.4.21.71`.

> The transition template points at `ghcr.io/snapetech-org/chaptarrng:latest` and
> keeps the existing `/config`, `/data`, `/download`, port 8787, PUID/PGID, TZ,
> and Hardcover settings. Do not publish or apply it until ChaptarrNG's
> version-aware SQLite fix is released and the Community Apps update path is
> validated. The current ChaptarrNG `v0.9.977` release accepts migration-158
> SQLite; upgrade BookshelfNG to `.71` first or wait for the follow-up release.

## Existing installations

Use the [BookshelfNG-to-ChaptarrNG migration guide](https://github.com/snapetech-org/bookshelfng/blob/main/docs/migrate-from-bookshelfng-to-chaptarrng.md).
Stop BookshelfNG, back up the complete appdata directory, and keep the same
media and download mounts. ChaptarrNG migrates the database on startup and
retains a BookshelfNG backup. The final BookshelfNG `.71` image can bring older
schemas to migration 158 before switching; ChaptarrNG `.977` rejects versions
before migration 14 until the follow-up fix is published.

An isolated Docker image-switch rehearsal used the published `.71` and `.977`
images with an empty migration-158 database. Startup conversion, source backup,
rollback, and a subsequent BookshelfNG start on port 8787 passed. This does not
validate populated operator data or the Community Apps template update flow.
Keep an independent backup until the converted library and external clients
have been checked.

New installations should use the
[ChaptarrNG Unraid template](https://github.com/snapetech-org/chaptarrng-unraid).
