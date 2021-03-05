import re


# Group a regular expression
def regex_groups(pattern: str, content: str) -> None:
    p = re.compile(pattern)
    match = p.search(content)
    print(match)
    print('Groups:', match.groups())
    print('Full match:', match.group())
    print('First group:', match.group(1))
    print('Second group:', match.group(2))
    print('Third group:', match.group(3))


if __name__ == '__main__':
    regex_groups(r'(\d{4})-(\d{2})-(\d{2})', '2016-01-01')
    print()

    # Nesting group
    regex_groups(r'(((\d{4})-\d{2})-\d{2})', '2016-01-01')
