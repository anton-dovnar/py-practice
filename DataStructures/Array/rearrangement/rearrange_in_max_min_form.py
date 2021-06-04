"""
Rearrange an array in maximum minimum form | Set 1

Given a sorted array of positive integers, rearrange the array
alternately i.e first element should be maximum value, second
minimum value, third second max, fourth second min and so on.

Time complexity: O(n)
Space complexity: O(1)
"""


def rearrange(arr: list):
    n = len(arr)
    max_el = arr[n - 1]
    min_el = arr[0]

    for i in range(n):
        if i % 2:
            arr[i] = min_el
            min_el += 1
        else:
            arr[i] = max_el
            max_el -= 1

    return arr


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(rearrange(arr))

    arr = [1, 2, 3, 4, 5, 6]
    print(rearrange(arr))

    arr = [1, 2, 3, 4, 5, 6, 7]
    print(rearrange(arr))
