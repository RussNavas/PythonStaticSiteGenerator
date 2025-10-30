from textnode import TextType, TextNode
from htmlnode import *


def main():
    original_text = "Text ![image](https://i.imgur.com/zjjcJKZ.png) more text ![image](https://i.imgur.com/zjjcJKZ.png) even more text."
    image_markdown = "![image](https://i.imgur.com/zjjcJKZ.png)"
    sections = original_text.split(image_markdown, 1)
    print(sections)


main()
