from enum import Enum
from markdown_to_blocks import markdown_to_blocks


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def block_to_block_type(block):
    if block[0] == "#":
        is_heading = False
        count = 0
        for c in block:
            if c == "#":
                count += 1
            if c == " ":
                is_heading = True
                break

        if count <= 6 and is_heading:
            return BlockType.HEADING

    elif block[0] == "`":
        is_code = False
        count = 0
        for c in block:
            if c == "`":
                count += 1
        if count == 6:
            is_code = True
        if is_code:
            return BlockType.CODE

    elif block[0] == ">":
        return BlockType.QUOTE

    elif block[0] == "-" and block[1] == " ":
        return BlockType.UNORDERED_LIST

    elif (block[0].isdigit()) and block[1] == ".":
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
