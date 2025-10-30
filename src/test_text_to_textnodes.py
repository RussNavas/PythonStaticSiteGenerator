from extract_markdown_images import extract_markdown_images
from extract_markdown_links import extract_markdown_links
from htmlnode import *
from textnode import TextNode, TextType
from split_nodes_image import split_nodes_images
from split_nodes_link import split_nodes_link
from text_node_to_html_node import text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter
from text_to_textnodes import text_to_textnodes
import unittest


class TestTextToTextNodes(unittest.TestCase):
    def test_1(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        res = text_to_textnodes(text)
        ans = [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        self.assertEqual(res, ans)
