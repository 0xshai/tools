#!/usr/bin/env python3
"""
从 bookmarks.yaml 自动生成 README.md
用法: python gen_readme.py
"""

import yaml

HEADER = """# 🛠️ tools

> 精选隐私友好、开源优先的实用工具清单。
> A curated list of privacy-friendly, open-source tools I actually use.

🔓 = 开源 / Open Source

---

"""

FOOTER = """
---

欢迎提 Issue 或 PR 推荐新工具。
"""

def generate_readme(yaml_path="bookmarks.yaml", output_path="README.md"):
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    lines = [HEADER]

    for category in data:
        icon = category.get("icon", "")
        name = category.get("category", "")
        items = category.get("items", [])

        lines.append(f"## {icon} {name}\n")
        lines.append("| 工具 | 描述 | 开源 |")
        lines.append("|------|------|------|")

        for item in items:
            tool_name = item.get("name", "")
            url = item.get("url", "")
            desc = item.get("desc", "")
            opensource = "🔓" if item.get("opensource") else ""
            lines.append(f"| [{tool_name}]({url}) | {desc} | {opensource} |")

        lines.append("")

    lines.append(FOOTER.strip())

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"✅ README.md 已生成，共 {len(data)} 个分类")

if __name__ == "__main__":
    generate_readme()
