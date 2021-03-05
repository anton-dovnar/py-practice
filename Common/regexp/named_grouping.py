import re

# Group reference `(?P<name>...)`
pattern = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')
match = pattern.search('2016-01-01')
print('Year group:', match.group('year'))
print('Month group:', match.group('month'))
print('Day group:', match.group('day'))

# Back reference by named group
pattern = re.compile(r'^(?P<char>[a-z])(?P=char)')
match = pattern.search('aa')
print(match is not None)
