import re
from typing import Union


def parse_html_tags(pattern: str, tag: str) -> Union[str, None]:
    p = re.compile(r'{}'.format(pattern))
    match = p.search(tag)
    return f'Found match: {match.group()}' if match else None


if __name__ == '__main__':
    tags = ['<table>', '<a href="#label">', '<img src="/img">', '</table>']
    pattern = '<[^/>][^>]*>'

    print('Open Tags')
    for tag in tags:
        print(parse_html_tags(pattern, tag))

    print('\nClose Tags')
    tags = [('</[^>]+>', '</table>'), ('<[^/>]+/>', '<br/>')]

    for pattern, tag in tags:
        print(parse_html_tags(pattern, tag))
