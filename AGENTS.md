# Repository Guidelines

## Project Structure & Module Organization

This repository is a personal profile and statistics asset repo. The main entry point is `README.md`, which renders the profile text and embeds local images. Store generated charts and screenshots in `png/`, portraits in `jpg/`, and animations in `gif/`. Keep helper scripts at the repository root: `qiao.sh` copies current time-statistic images from the neighboring Notion project, and `guan.sh` opens the README for editing. `imgurl.md` stores external image URL notes.

## Build, Test, and Development Commands

There is no package manager, build step, or automated test suite. Use these commands for routine work:

```sh
sh qiao.sh
```

Copies the configured daily PNG files from `../notion/time/png/` into `./png/`. Edit `year`, `month`, `day`, and `week` in the script before running.

```sh
sh guan.sh
```

Opens `README.md` in Vim for manual updates.

```sh
git status --short
```

Review changed images and Markdown before committing.

## Coding Style & Naming Conventions

Keep Markdown concise and readable. The README currently uses Chinese section headings, short bullet lists, Markdown tables, and inline HTML `<img>` tags for precise image sizing. Preserve that style when updating content. Name statistic assets consistently, for example `new_YYYYMMDD_pie.png`, `new_YYYYMMDD_plot.png`, `YYYYMMweekNN_table.png`, and `YYYYMM_work_time.png`. Shell scripts should remain simple POSIX-style scripts with clear variable assignments near the top.

## Testing Guidelines

Validate changes by previewing `README.md` in GitHub or a Markdown viewer. Confirm that every referenced local image exists under the expected directory and that image widths still total roughly 100% for each row. After running `qiao.sh`, use `ls -lh png/<pattern>` to verify copied files.

## Commit & Pull Request Guidelines

Recent commits use short messages such as `daily update` and `cc:update code`. Prefer concise, imperative messages that describe the visible change, for example `daily update` for routine statistic refreshes or `update June charts` for asset-specific edits. Pull requests should summarize changed README content, list added or removed image files, and include a rendered screenshot when layout changes affect the profile display.

## Asset Hygiene

Do not commit temporary exports, duplicate charts, or unrelated local files. Before committing, check that `.gitignore` still tracks only the intended root files and asset directories, and avoid renaming historical PNGs unless the README references are updated at the same time.

## Daily Record Update Workflow

When the user says `更新今日记录`, `更新今天记录`, `更新日记录`, or similar wording, execute this workflow directly. Use a date supplied by the user if present; otherwise use the newest `new_YYYYMMDD_*.png` files in `../notion/time/png/`.

1. Update `qiao.sh` variables (`year`, `month`, `day`, and `week`) for the target date, then run `sh qiao.sh` to copy daily images into `png/`.
2. Check whether weekly files exist in `../notion/time/png/`, especially `${year}${month}week${week}_table.png`, `${year}${month}week${week}_emotion.png`, and `${year}${month}week${week}_location_pie.png`. If a newer complete weekly set exists, copy it into `png/` and update the README week section. Use the project’s Sunday-Saturday week range style, for example `2026.05.31-2026.06.06`.
3. Check whether monthly files exist for the current month: `${year}${month}_pie.png`, `${year}${month}_location_pie.png`, and `${year}${month}_work_time.png`. If the complete set exists and is newer than README, copy it into `png/` and update the README month section using `YYYY.MM.01-YYYY.MM.last_day`.
4. Update `README.md` daily date and image references to the target date. Update week/month sections only when the corresponding complete image sets are available.
5. Verify copied files with `ls -lh`, inspect `git diff`, then commit all resulting changes with `git commit -m "daily update"` and push to `origin/main`.
