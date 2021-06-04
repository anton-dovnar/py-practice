"""
Reorder an arrya according to given indexes

Given two integer arrays of same size, “arr[]” and “index[]”,
reorder elements in “arr[]” according to given index array.
It is not allowed to given array arr’s length.

Time complexity: O(n)
Space complexity: O(1)
"""


def rearrange(arr: list, indexes: list) -> list:
    for i in range(len(arr)):
        if indexes[i] != i:
            arr[indexes[i]], arr[i] = arr[i], arr[indexes[i]]
            indexes[indexes[i]], indexes[i] = indexes[i], indexes[indexes[i]]
    print(arr)
    print(indexes)
    return arr, indexes


if __name__ == '__main__':
    arr = [10, 11, 12]
    indexes = [1, 0, 2]
    assert rearrange(arr, indexes) == ([11, 10, 12], [0, 1, 2])

    arr = [50, 40, 70, 60, 90]
    indexes = [3, 0, 4, 1, 2]
    assert rearrange(arr, indexes) == ([40, 60, 90, 50, 70], [0, 1, 2, 3, 4])
