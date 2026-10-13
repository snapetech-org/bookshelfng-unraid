# BookshelfNG Unraid retirement template

The final BookshelfNG source release is `0.4.21.71`. This legacy template is
being prepared to transition existing installations to the standard ChaptarrNG
image while preserving their appdata and media paths.

## Migration status

The transition template points to
`ghcr.io/snapetech-org/chaptarrng:latest` and keeps `/config`, `/data`,
`/download`, port 8787, PUID/PGID, timezone, and existing Hardcover variables.
Do not apply it until the version-aware ChaptarrNG SQLite fix is released and
the Community Apps upgrade path is validated. ChaptarrNG `v0.9.977` accepts
migration-158 SQLite. Upgrade BookshelfNG to `.71` first, or wait for the
follow-up release before switching an older database.

Follow the
[operator migration guide](https://github.com/snapetech-org/bookshelfng/blob/main/docs/migrate-from-bookshelfng-to-chaptarrng.md).
Stop BookshelfNG, create an independent full appdata backup, and keep all media
and download mappings. ChaptarrNG migrates a supported database on first
startup and retains the source database. The old image and backup must remain
available until conversion, library contents, and client behavior are checked.

An isolated Docker image-switch rehearsal converted and restored an empty
migration-158 database with the `.71` BookshelfNG and `.977` ChaptarrNG images.
The old image started again on port 8787. The Community Apps template update
flow and populated operator data remain untested.

New installations should use the
[ChaptarrNG Unraid template](https://github.com/snapetech-org/chaptarrng-unraid).
