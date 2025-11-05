import unittest
from textnode import *
from htmlnode import *
from text_node_to_html_node import *
from split_nodes_delimiter import *


class Test_split_nodes_delimiter(unittest.TestCase):
    def test_mixed_lst_1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        node_lst = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, node_lst)

