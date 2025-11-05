import unittest
from htmlnode import HTMLNode, LeafNode


class TestLeafNode(unittest.TestCase):
    def test_is_eq(self):
        example = "<p>This is a paragraph of text.</p>"
        res = LeafNode("p", "This is a paragraph of text.").to_html()
        self.assertEqual(example, res)

    def test_is_eq2(self):
        example = '<a href="https://www.google.com">Click me!</a>'
        res = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(example, res)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")




# ---------- END TEST----------------------

if __name__ == "__main__":
    unittest.main()