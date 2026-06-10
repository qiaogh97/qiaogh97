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
