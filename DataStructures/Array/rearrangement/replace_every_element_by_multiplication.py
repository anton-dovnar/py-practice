"""
Replace every array elemnt by multiplication of previous and next

Given an array of integers, update every element with multiplication
of previous and next elements with following exceptions.
a) First element is replaced by multiplication of first and second.
b) Last element is replaced by multiplication of last and second last.

Time complexity: O(n)
Space complexity: O(1)
"""


def rearrange(arr: list) -> list:
    n = len(arr)
    prev = arr[0]
    arr[0] = arr[0] * arr[1]

    for i in range(1, n - 1):
        curr = arr[i]
        arr[i] = prev * arr[i + 1]
        prev = curr

    arr[n - 1] = prev * arr[n - 1]
    return arr


if __name__ == '__main__':
    arr = [2, 3, 4, 5, 6]
    assert rearrange(arr) == [6, 8, 15, 24, 30]
