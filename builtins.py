import builtins
from collections import defaultdict

CBLUEBG2 = '\33[104m'
CYELLOW2 = '\33[93m'
CBOLD = '\33[1m'
CEND = '\33[0m'

types = defaultdict(list)

for i in dir(builtins):
    types[type(getattr(builtins, i))].append(i)

for key, val in types.items():
    print(f'{CBLUEBG2}{key}:{CEND}')
    node_len = len(val)
    print(f'\t{CYELLOW2}Length {node_len}{CEND}', end=":")
    for k, v in enumerate(val):
        if k % 5 == 0:
            print('\n\t\t', end="")
        print(f'{CBOLD}{v}{CEND}', end=", ")
    print('\n')
