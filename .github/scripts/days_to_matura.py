#!/usr/bin/env python3
"""Generate a "days to matura" badge (SVG) + JSON for the matura.lol org README.

Mirrors the countdown logic in search.matugen web/app.js:
  matura starts 3 May; if today is past it, target next year;
  days = round((target - today) / 86400000).

Writes:
  - assets/days-to-matura.svg   shields.io-style badge "Do matury: N dni"
  - days-to-matura.json         { days, date, matura_date }
"""
import datetime as dt
import json
import os
import xml.sax.saxutils as sax

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))  # .github/scripts -> repo root

LEFT = "#14161a"    # matura.lol dark bg
RIGHT = "#4c8dff"   # matura.lol accent
GREEN = "#16a34a"


def days_to_matura(now: dt.date) -> tuple[int, dt.date]:
    target = dt.date(now.year, 5, 3)  # 3 May
    if now > target:
        target = dt.date(now.year + 1, 5, 3)
    return round((target - now).total_seconds() / 86400), target


def _text_w(chars: int) -> int:
    return 12 + chars * 8


def badge(left: str, right: str, color: str, today: bool = False) -> str:
    lw = _text_w(len(left))
    rw = _text_w(len(right))
    width = lw + rw
    lcx = lw / 2
    rcx = lw + rw / 2
    left_s = sax.escape(left)
    right_s = sax.escape(right)
    sub = sax.escape("Dziś matura!" if today else "")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="28" role="img" aria-label="{left_s}: {right_s}">
  <title>{left_s}: {right_s}</title>
  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-opacity=".1" stop-color="#fff"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <clipPath id="r"><rect width="{width}" height="28" rx="5" fill="#fff"/></clipPath>
  <g clip-path="url(#r)">
    <rect width="{lw}" height="28" fill="{LEFT}"/>
    <rect x="{lw}" width="{rw}" height="28" fill="{color}"/>
    <rect width="{width}" height="28" fill="url(#s)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="13">
    <text x="{lcx}" y="18.5" font-weight="bold">{left_s}</text>
    <text x="{rcx}" y="18.5" font-weight="bold">{right_s}</text>
  </g>
  <g fill="#ffffff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="9">
    <text x="{rcx}" y="25.5" opacity="0.85">{sub}</text>
  </g>
</svg>'''


def main() -> None:
    today = dt.date.today()
    days, target = days_to_matura(today)
    today_flag = days <= 0
    if today_flag:
        label = "Dziś matura!"
    else:
        label = f"{days} dni"
    svg = badge("Do matury", label, GREEN if today_flag else RIGHT, today_flag)

    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    with open(os.path.join(ROOT, "assets", "days-to-matura.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    with open(os.path.join(ROOT, "days-to-matura.json"), "w", encoding="utf-8") as f:
        json.dump(
            {"days": max(days, 0), "date": today.isoformat(),
             "matura_date": target.isoformat(), "today": today_flag},
            f, indent=2, ensure_ascii=False)
    print(f"days={days} target={target.isoformat()} -> assets/days-to-matura.svg + days-to-matura.json")


if __name__ == "__main__":
    main()