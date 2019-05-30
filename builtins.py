import builtins
from collections import defaultdict

types = defaultdict(list)

for i in dir(builtins):
    types[type(getattr(builtins, i))].append(i)

for key, val in types.items():
    print(key, end=" :")
    print('\n\tLength', len(val), end=": ")
    for k, v in enumerate(val):
        if k % 10 == 0:
            print()
            print('\t', end="")
        print(v, end=", ")
    print()
