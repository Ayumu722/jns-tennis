#!/usr/bin/env python3
"""content.yaml / content.en.yaml から index.html を生成する。"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / "index.html.template"

LOCALES = (
    {
        "lang": "ja",
        "content": ROOT / "content.yaml",
        "output": ROOT / "index.html",
        "asset_prefix": "",
        "lang_switch": {"href": "en/", "lang": "en"},
        "hreflang": {"ja": "./", "en": "en/"},
    },
    {
        "lang": "en",
        "content": ROOT / "content.en.yaml",
        "output": ROOT / "en" / "index.html",
        "asset_prefix": "../",
        "lang_switch": {"href": "../", "lang": "ja"},
        "hreflang": {"ja": "../", "en": "./"},
    },
)


def main() -> int:
    try:
        import yaml
        from jinja2 import Environment, FileSystemLoader, select_autoescape
    except ImportError:
        print("エラー: 依存パッケージがありません")
        print("  pip install -r requirements.txt")
        return 1

    if not TEMPLATE.is_file():
        print(f"エラー: {TEMPLATE.name} が見つかりません")
        return 1

    env = Environment(
        loader=FileSystemLoader(ROOT),
        autoescape=select_autoescape(["html", "xml"]),
        keep_trailing_newline=True,
    )
    template = env.get_template(TEMPLATE.name)

    print(f"テンプレート: {TEMPLATE.name}")
    for i, loc in enumerate(LOCALES, 1):
        if not loc["content"].is_file():
            print(f"エラー: {loc['content'].name} が見つかりません")
            return 1
        print(f"[{i}/{len(LOCALES)}] 読込: {loc['content'].name} ({loc['lang']})")
        data = yaml.safe_load(loc["content"].read_text(encoding="utf-8"))
        html = template.render(
            lang=loc["lang"],
            asset_prefix=loc["asset_prefix"],
            lang_switch=loc["lang_switch"],
            hreflang=loc["hreflang"],
            **data,
        )
        loc["output"].parent.mkdir(parents=True, exist_ok=True)
        loc["output"].write_text(html, encoding="utf-8")
        print(f"      出力: {loc['output'].relative_to(ROOT)}")

    print("完了")
    return 0


if __name__ == "__main__":
    sys.exit(main())
