"""
Arrange given numbers to form the biggest nubmer

Given an array of numbers, arrange them in a way that yields the
largest value. For example, if the given numbers are {54, 546, 548, 60},
the arrangement 6054854654 gives the largest value. And if the given numbers
are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the
largest value.

Time complexity: O(n log n)
"""
from itertools import permutations


def arrange(arr: list):
    result = []
    for i in permutations(arr, len(arr)):
        result.append("".join(map(str, i)))
    return max(result)


if __name__ == '__main__':
    arr = [54, 546, 548, 60]
    print(arrange(arr))
