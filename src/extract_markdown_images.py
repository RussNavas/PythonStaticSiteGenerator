import re


def extract_markdown_images(text):
    '''
        text -> str of raw markdown
        :return: [(tuple)] where tuple is (alt text, url)
    '''
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
