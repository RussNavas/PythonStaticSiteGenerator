from textnode import *
from htmlnode import *


def text_node_to_html_node(text_node):
    '''
    TextTypes Enum:
        TEXT = "text"
        BOLD = "bold"
        ITALIC = "italic"
        CODE = "code"
        LINK = "link"
        IMAGE = "image"
    '''
    if text_node.text_type.value == "text":
        return LeafNode(None, value=text_node.text)
    elif text_node.text_type.value == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type.value == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type.value == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type.value == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type.value == "image":
        return LeafNode("img", "", {"src": text_node.url,
                                    "alt": text_node.text})
    else:
        raise ValueError(f"invalid text type: {text_node.text_type}")
