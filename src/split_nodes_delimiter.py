from htmlnode import *
from textnode import *
from text_node_to_html_node import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    '''
        old_nodes -> [textnode objects]
        delimiter -> str
        text_type -> member of enum

        recall: TextType Enum:
                TEXT = "text"
                BOLD = "bold"
                ITALIC = "italic"
                CODE = "code"
                LINK = "link"
                IMAGE = "image"
        :returns: [nodes(that may be derived from a single text type node)]
    '''

    new_lst = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_lst.append(old_node)
            continue

        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise SyntaxError(
                "Incorrect Markdown syntax: missing delimiter(s)."
            )
        for i, part in enumerate(parts):
            if i % 2 == 0 and part == "":
                continue
            if i % 2 == 0:
                new_node = TextNode(part, TextType.TEXT)
                new_lst.append(new_node)
            else:
                new_node = TextNode(part, text_type)
                new_lst.append(new_node)
    return new_lst
