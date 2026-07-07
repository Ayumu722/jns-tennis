#!/usr/bin/env python3
"""content.yaml から index.html を生成する。"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content.yaml"
TEMPLATE = ROOT / "index.html.template"
OUTPUT = ROOT / "index.html"


def main() -> int:
    try:
        import yaml
        from jinja2 import Environment, FileSystemLoader, select_autoescape
    except ImportError:
        print("エラー: 依存パッケージがありません")
        print("  pip install -r requirements.txt")
        return 1

    for path in (CONTENT, TEMPLATE):
        if not path.is_file():
            print(f"エラー: {path.name} が見つかりません")
            return 1

    print(f"[1/3] 読込: {CONTENT.name}")
    data = yaml.safe_load(CONTENT.read_text(encoding="utf-8"))

    print(f"[2/3] テンプレート適用: {TEMPLATE.name}")
    env = Environment(
        loader=FileSystemLoader(ROOT),
        autoescape=select_autoescape(["html", "xml"]),
        keep_trailing_newline=True,
    )
    html = env.get_template(TEMPLATE.name).render(**data)

    print(f"[3/3] 出力: {OUTPUT.name}")
    OUTPUT.write_text(html, encoding="utf-8")
    print("完了")
    return 0


if __name__ == "__main__":
    sys.exit(main())
