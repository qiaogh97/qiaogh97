# 习惯打卡

主页中的绿色方格由 `data/habits.json` 生成：每个方格对应一天，绿色表示完成，灰色表示未完成或尚未记录。累计天数只计算完成的记录。

推荐在 GitHub 网页中打卡：进入仓库的 **Actions → Habit check-in → Run workflow**，选择两个习惯是否完成；日期留空即为上海当天。工作流会自动更新数据和主页图。

如需补录，可填写日期，例如 `2026-08-21`。也可以本地执行：

```sh
python3 scripts/render_habits.py --date 2026-08-21 --wake yes --exercise no
```

数据是明确的每日记录；请只填写真实完成的日期。
