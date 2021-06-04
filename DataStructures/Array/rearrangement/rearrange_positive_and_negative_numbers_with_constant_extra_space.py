"""
Rearrange positive and negative numbers with constant extra space

Given an array of positive and negative numbers, arrange them such that all
negative integers appear before all the positive integers in the array without
using any additional data structure like hash table, arrays, etc.

Time complexity: O(n)
Space complexity: O(1)
"""


def rearrange(arr: list) -> list:
    count = 0  # Count negative numbers
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1

    return arr


if __name__ == '__main__':
    arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
    print(rearrange(arr))
