#!/usr/bin/env python3
"""Render the profile habit grid from data/habits.json."""

from __future__ import annotations

import argparse
import json
from datetime import date, datetime, timedelta
from html import escape
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "habits.json"
OUTPUT_FILE = ROOT / "assets" / "habit-activity.svg"
WEEKS = 53
CELL = 13
GAP = 3
LEFT = 105
# The grid has no heading or legend, so it can begin near the top edge.
TOP = 20


def shanghai_today() -> date:
    return datetime.now(ZoneInfo("Asia/Shanghai")).date()


def load_data() -> dict:
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def write_data(data: dict) -> None:
    DATA_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def render(data: dict) -> str:
    today = shanghai_today()
    # Start on Sunday so the grid reads like GitHub's contribution graph.
    end = today + timedelta(days=(6 - (today.weekday() + 1) % 7))
    start = end - timedelta(days=WEEKS * 7 - 1)
    habits = list(data["habits"].items())
    records = data.get("records", {})
    width = LEFT + WEEKS * (CELL + GAP) + 24
    habit_height = 7 * (CELL + GAP)
    row_gap = 28
    height = TOP + len(habits) * (habit_height + row_gap) + 24
    total_days = {name: sum(1 for item in records.values() if item.get(name)) for name, _ in habits}

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="Habit activity">',
        '<rect width="100%" height="100%" rx="10" fill="#ffffff"/>',
    ]
    for row, (name, habit) in enumerate(habits):
        y = TOP + row * (habit_height + row_gap)
        label = escape(habit["label"])
        elements.append(
            f'<text x="20" y="{y + 48}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="13" fill="#24292f">{label}</text>'
        )
        elements.append(
            f'<text x="20" y="{y + 65}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="12" fill="#57606a">累计 {total_days[name]} 天</text>'
        )
        for offset in range(WEEKS * 7):
            current = start + timedelta(days=offset)
            col, day_of_week = divmod(offset, 7)
            x = LEFT + col * (CELL + GAP)
            cell_y = y + day_of_week * (CELL + GAP)
            done = bool(records.get(current.isoformat(), {}).get(name))
            fill = "#39d353" if done else "#ebedf0"
            opacity = "1" if current <= today else "0.45"
            elements.append(
                f'<rect x="{x}" y="{cell_y}" width="{CELL}" height="{CELL}" rx="2" fill="{fill}" opacity="{opacity}"><title>{current.isoformat()}: {label} {"完成" if done else "未完成"}</title></rect>'
            )
    elements.extend([
        f'<text x="{LEFT}" y="{height - 12}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="11" fill="#57606a">{start.isoformat()}</text>',
        f'<text x="{width - 94}" y="{height - 12}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="11" fill="#57606a">{today.isoformat()}</text>',
        '</svg>',
    ])
    return "\n".join(elements) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="Date to update (YYYY-MM-DD); defaults to Asia/Shanghai today.")
    parser.add_argument("--wake", choices=("yes", "no"), help="Whether 06:10 wake-up was completed.")
    parser.add_argument("--exercise", choices=("yes", "no"), help="Whether 30m exercise was completed.")
    args = parser.parse_args()
    data = load_data()
    if args.wake or args.exercise:
        record_date = date.fromisoformat(args.date) if args.date else shanghai_today()
        record = data.setdefault("records", {}).setdefault(record_date.isoformat(), {})
        if args.wake:
            record["wake_0610"] = args.wake == "yes"
        if args.exercise:
            record["exercise_30m"] = args.exercise == "yes"
        write_data(data)
    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(render(data), encoding="utf-8")


if __name__ == "__main__":
    main()
