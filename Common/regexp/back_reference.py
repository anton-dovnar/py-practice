import re

# Compare `aa`, `bb`
pattern = re.compile(r'([a-z])\1$')
match = pattern.search('aa')
print(match is not None)

match = pattern.search('bb')
print(match is not None)

match = pattern.search('ab')
print(match is not None)

# Compare open tag and close tag
pattern = re.compile(r'<([^>]+)>[\s\S]*?</\1>')
match = pattern.search('<bold> test </bold>')
print(match is not None)

match = pattern.search('<h1> heading </h1>')
print(match is not None)

match = pattern.search('<bold> test </h1>')
print(match is not None)
