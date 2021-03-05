import re
import urllib.request
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

    tags = [('</[^>]+>', '</table>'), ('<[^/>]+/>', '<br/>')]
    print('\nClose Tags')

    for pattern, tag in tags:
        print(parse_html_tags(pattern, tag))

    # parse python.org
    with urllib.request.urlopen('https://www.python.org') as resp:
        html = resp.read()

    print('\npython.org first five open tags:')
    print(re.findall(r'<[^/>][^>]*>', html.decode('utf-8'))[:5])

    print('\npython.org first five close tags')
    print(re.findall(r'</[^>]+>', html.decode('utf-8'))[:5])
