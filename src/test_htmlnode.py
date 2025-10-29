import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_null_node(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_node_eq(self):
        node = HTMLNode("<a>",
                        "www.google.com",
                        [HTMLNode(),
                         HTMLNode()
                         ],
                        {"href": "./some_uri"}
                        )

        node2 = HTMLNode("<a>",
                         "www.google.com",
                         [HTMLNode(),
                          HTMLNode()
                          ],
                         {"href": "./some_uri"}
                         )
        self.assertEqual(node, node2)

    def test_node_not_equal(self):
        node = HTMLNode("<a>",
                        "www.bing.com",
                        [HTMLNode(),
                         HTMLNode()
                         ],
                        {"href": "./some_uri"}
                        )

        node2 = HTMLNode("<a>",
                         "www.google.com",
                         [HTMLNode(),
                          HTMLNode()
                          ],
                         {"href": "./some_uri"}
                         )
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("<a>",
                        "www.bing.com",
                        [HTMLNode(),
                         HTMLNode()
                         ],
                        {"href": "./some_uri"}
                        )
        message = ' href="./some_uri"'
        res = node.props_to_html()
        self.assertEqual(res, message)
# ---------- END TEST----------------------


if __name__ == "__main__":
    unittest.main()
