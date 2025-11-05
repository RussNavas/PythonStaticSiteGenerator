import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node


def _is_hidden(name: str) -> bool:
    # Skip macOS & other dotfiles, e.g. .DS_Store, .gitkeep, ._Resource
    return name.startswith(".") or name.startswith("._")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        if _is_hidden(filename):
            continue

        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            if not filename.lower().endswith(".md"):
                continue
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    try:
        title = extract_title(markdown_content)
    except ValueError:
        title = os.path.splitext(os.path.basename(from_path))[0].replace("-", " ").replace("_", " ").title()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
