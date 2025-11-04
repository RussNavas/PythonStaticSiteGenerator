from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType


def markdown_to_html_node(markdown):

    root = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)

    for block in blocks:

        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            count = 0
            for c in block:
                if c == "#":
                    count += 1
                if c == " ":
                    break
            tag = f"h{count}"
            parent = ParentNode(tag, [])
            text = block[count+1:]
            textnodes = text_to_textnodes(text)
            for textnode in textnodes:
                parent.children.append(text_node_to_html_node(textnode))
            root.children.append(parent)

        elif block_type == BlockType.PARAGRAPH:
            parent = ParentNode("p", [])
            text = block.split("\n")
            text = " ".join([line.strip() for line in text])
            textnodes = text_to_textnodes(text)
            for textnode in textnodes:
                parent.children.append(text_node_to_html_node(textnode))
            root.children.append(parent)

        elif block_type == BlockType.QUOTE:
            parent = ParentNode("blockquote", [])
            text_split = block.split("\n")
            text_cleaned = [line.strip("> ") for line in text_split]
            text = " ".join(text_cleaned)
            textnodes = text_to_textnodes(text)
            for textnode in textnodes:
                parent.children.append(text_node_to_html_node(textnode))
            root.children.append(parent)

        elif block_type == BlockType.ORDERED_LIST:
            outer_parent = ParentNode("ol", [])
            list_items = block.split("\n")
            for item in list_items:
                inner_parent = ParentNode("li", [])
                textnodes = text_to_textnodes(item[3:])
                for textnode in textnodes:
                    inner_parent.children.append(text_node_to_html_node(textnode))
                outer_parent.children.append(inner_parent)
            root.children.append(outer_parent)

        elif block_type == BlockType.UNORDERED_LIST:
            outer_parent = ParentNode("ul", [])
            list_items = block.split("\n")
            for item in list_items:
                inner_parent = ParentNode("li", [])
                textnodes = text_to_textnodes(item[2:])
                for textnode in textnodes:
                    inner_parent.children.append(text_node_to_html_node(textnode))
                outer_parent.children.append(inner_parent)
            root.children.append(outer_parent)

        elif block_type == BlockType.CODE:
            pre_parent = ParentNode("pre", [])
            split_block = block.split("\n")
            new_lst = [line.strip() for line in split_block[1:-1]]
            joined_block = "\n".join(new_lst)
            joined_block += "\n"  # Add trailing newline
            text_node = TextNode(joined_block, TextType.TEXT)
            html_node = text_node_to_html_node(text_node)
            code_parent = ParentNode("code", [html_node])
            pre_parent.children.append(code_parent)
            root.children.append(pre_parent)
    return root
