from extract_markdown_links import extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_link(old_nodes):
    res = []

    for node in old_nodes:
        if node.text == "" or node.text is None:
            continue
        if node.text_type != TextType.TEXT:
            res.append(node)
            continue
        matches = extract_markdown_links(node.text)
        if not matches:
            res.append(node)
            continue
        current_text_to_process = node.text
        for match in matches:
            current_sections = current_text_to_process.split(f"[{match[0]}]({match[1]})", 1)
            text_before_link = current_sections[0]
            text_after_link = current_sections[1]
            if text_before_link:
                new_node = TextNode(text_before_link, TextType.TEXT)
                res.append(new_node)
            link_node = TextNode(match[0], TextType.LINK, match[1])
            res.append(link_node)
            current_text_to_process = text_after_link
        if current_text_to_process:
            new_node = TextNode(current_text_to_process, TextType.TEXT)
            res.append(new_node)
    return res
