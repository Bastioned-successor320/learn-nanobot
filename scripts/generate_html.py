#!/usr/bin/env python3
"""
将 learn-nanobot 项目的所有 Markdown 文档转换为 HTML 格式。

使用方法:
    pip install markdown
    python scripts/generate_html.py

输出目录: output/html/
"""

import os
import shutil
from pathlib import Path

try:
    import markdown
except ImportError:
    print("请先安装 markdown: pip install markdown")
    exit(1)

PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
OUTPUT_DIR = PROJECT_ROOT / "output" / "html"
COMICS_DIR = PROJECT_ROOT / "comics"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Learn Nanobot 面试学习指南</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC',
                         'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
            line-height: 1.8;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px 40px;
            background: #fafafa;
        }}
        h1 {{ color: #1a1a2e; border-bottom: 3px solid #0066cc; padding-bottom: 10px; margin: 30px 0 20px; }}
        h2 {{ color: #16213e; border-bottom: 1px solid #ddd; padding-bottom: 8px; margin: 25px 0 15px; }}
        h3 {{ color: #0f3460; margin: 20px 0 10px; }}
        h4 {{ color: #533483; margin: 15px 0 8px; }}
        code {{
            background: #f0f0f0; padding: 2px 6px; border-radius: 3px;
            font-family: 'JetBrains Mono', 'Fira Code', monospace; font-size: 0.9em;
        }}
        pre {{
            background: #1e1e1e; color: #d4d4d4; padding: 16px; border-radius: 8px;
            overflow-x: auto; margin: 15px 0; line-height: 1.5;
        }}
        pre code {{ background: transparent; color: inherit; padding: 0; }}
        table {{
            border-collapse: collapse; width: 100%; margin: 15px 0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        th {{ background: #0066cc; color: white; padding: 10px 15px; text-align: left; }}
        td {{ padding: 10px 15px; border-bottom: 1px solid #eee; }}
        tr:nth-child(even) {{ background: #f8f9fa; }}
        tr:hover {{ background: #e8f4fd; }}
        blockquote {{
            border-left: 4px solid #0066cc; padding: 10px 20px; margin: 15px 0;
            background: #f0f7ff; border-radius: 0 4px 4px 0;
        }}
        img {{ max-width: 100%; height: auto; border-radius: 8px; margin: 15px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
        a {{ color: #0066cc; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .nav {{
            background: #1a1a2e; color: white; padding: 15px 20px;
            border-radius: 8px; margin-bottom: 30px;
        }}
        .nav a {{ color: #7ec8e3; margin: 0 10px; }}
        em {{ color: #666; }}
        hr {{ border: none; border-top: 1px solid #ddd; margin: 20px 0; }}
        ul, ol {{ padding-left: 25px; }}
        li {{ margin: 5px 0; }}
    </style>
</head>
<body>
    <div class="nav">
        <a href="../index.html">首页</a> |
        <a href="../index.html">目录</a> |
        <a href="https://github.com/bcefghj/learn-nanobot">GitHub</a>
    </div>
    {content}
    <hr>
    <p style="text-align: center; color: #999; margin-top: 30px;">
        Learn Nanobot 面试学习指南 | MIT License |
        <a href="https://github.com/bcefghj/learn-nanobot">GitHub</a>
    </p>
</body>
</html>"""

def convert_md_to_html(md_path: Path, output_path: Path, title: str):
    md_content = md_path.read_text(encoding="utf-8")
    html_content = markdown.markdown(
        md_content,
        extensions=["tables", "fenced_code", "toc", "attr_list"],
    )
    full_html = HTML_TEMPLATE.format(title=title, content=html_content)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(full_html, encoding="utf-8")
    print(f"  Generated: {output_path.relative_to(PROJECT_ROOT)}")


def main():
    print("=" * 60)
    print("Learn Nanobot - HTML Generator")
    print("=" * 60)

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    comics_out = OUTPUT_DIR / "comics"
    if COMICS_DIR.exists():
        shutil.copytree(COMICS_DIR, comics_out)
        print(f"  Copied comics to {comics_out.relative_to(PROJECT_ROOT)}")

    readme = PROJECT_ROOT / "README.md"
    if readme.exists():
        convert_md_to_html(readme, OUTPUT_DIR / "index.html", "首页")

    for doc_dir in sorted(DOCS_DIR.iterdir()):
        if not doc_dir.is_dir():
            continue
        readme = doc_dir / "README.md"
        if readme.exists():
            title = doc_dir.name.replace("-", " ").title()
            out_path = OUTPUT_DIR / doc_dir.name / "index.html"
            convert_md_to_html(readme, out_path, title)

    print(f"\nDone! HTML files generated in: {OUTPUT_DIR}")
    print(f"Open {OUTPUT_DIR / 'index.html'} to start reading.")


if __name__ == "__main__":
    main()
