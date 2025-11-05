import unittest
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType

md1 = '''
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
'''

md2 = '''
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
'''

md2_blocks = [
    "This is **bolded** paragraph",
    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
    "- This is a list\n- with items",
    ]


class TestBlockToBlockType(unittest.TestCase):

    # ------ HEADINGS -------
    def test_headings1(self):
        md = "# THIS IS A HEADING \n\n"
        blocks = markdown_to_blocks(md)
        res = block_to_block_type(blocks[0])
        self.assertEqual(res, BlockType.HEADING)

    def test_headings2(self):
        md = "## THIS IS A HEADING \n\n"
        blocks = markdown_to_blocks(md)
        res = block_to_block_type(blocks[0])
        self.assertEqual(res, BlockType.HEADING)

    def test_headings3(self):
        md = "### THIS IS A HEADING \n\n"
        blocks = markdown_to_blocks(md)
        res = block_to_block_type(blocks[0])
        self.assertEqual(res, BlockType.HEADING)

    def test_headings4(self):
        md = "#### THIS IS A HEADING \n\n"
        blocks = markdown_to_blocks(md)
        res = block_to_block_type(blocks[0])
        self.assertEqual(res, BlockType.HEADING)

    def test_headings5(self):
        md = "##### THIS IS A HEADING \n\n"
        blocks = markdown_to_blocks(md)
        res = block_to_block_type(blocks[0])
        self.assertEqual(res, BlockType.HEADING)

    def test_headings6(self):
        md = "###### THIS IS A HEADING \n\n"
        blocks = markdown_to_blocks(md)

        res = block_to_block_type(blocks[0])
        self.assertEqual(res, BlockType.HEADING)

    def test_headings7(self):
        md = "####### THIS IS NOT VALID A HEADING \n\n"
        blocks = markdown_to_blocks(md)
        res = block_to_block_type(blocks[0])
        self.assertNotEqual(res, BlockType.HEADING)

    # ------ code -------
    def test_code1(self):
        md = "``` This is code ``` \n\n"
        blocks = markdown_to_blocks(md)
        res = block_to_block_type(blocks[0])
        self.assertEqual(res, BlockType.CODE)

    # ------ quote -------
    def test_quote1(self):
        md = "> a quote \n\n"
        blocks = markdown_to_blocks(md)
        res = block_to_block_type(blocks[0])
        self.assertEqual(res, BlockType.QUOTE)

    # ------ UL -------
    def test_UL1(self):
        md = "- this is an ul item \n\n"
        blocks = markdown_to_blocks(md)
        res = block_to_block_type(blocks[0])
        self.assertEqual(res, BlockType.UNORDERED_LIST)

    # ------ OL -------
    def test_OL1(self):
        md = "1. this is an ol item \n\n"
        blocks = markdown_to_blocks(md)
        res = block_to_block_type(blocks[0])
        self.assertEqual(res, BlockType.ORDERED_LIST)

    # ------ para -------
    def test_para(self):
        md = "this is a para \n\n"
        blocks = markdown_to_blocks(md)
        res = block_to_block_type(blocks[0])
        self.assertEqual(res, BlockType.PARAGRAPH)
