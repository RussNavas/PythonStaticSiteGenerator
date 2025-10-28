from textnode import TextType, TextNode


def main():
    text_type = TextType.BOLD
    text_node = TextNode("some text",
                         text_type,
                         "www.google.com")
    print(text_node)


main()
