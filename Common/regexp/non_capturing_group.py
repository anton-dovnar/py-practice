import re


url = 'http://stackoverflow.com/'

# Non capturing group
pattern = re.compile(r'(?:http|ftp)://([^/\r\n]+)(/[^\r\n]*)?')
match = pattern.search(url)
print('Non capturing groups:', match.groups())

# Capturing groups
pattern = re.compile(r'(http|ftp)://([^/\r\n]+)(/[^\r\n]*)?')
match = pattern.search(url)
print('Capturing groups:', match.groups())
