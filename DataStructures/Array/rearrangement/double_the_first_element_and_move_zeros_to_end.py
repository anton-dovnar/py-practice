"""
Double the first element and move zero to end.

For a given array of n integers and assume that ‘0’ is an invalid number
and all others as a valid number. Convert the array in such a way that if
both current and next element is valid then double current value and replace
the next number with 0. After the modification, rearrange the array such
that all 0’s shifted to the end.

Time complexity: O(n)
Space comlexity: O(1)
"""


def rearrange(arr, n):
    if n < 2:
        return arr

    count = 0  # Count of non-zero elements
    for i in range(0, n - 1):
        if arr[i] != 0 and arr[i] == arr[i + 1]:
            arr[i] = 2 * arr[i]
            arr[i + 1] = 0

        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1

    arr[count], arr[n - 1] = arr[n - 1], arr[count]
    print(arr)
    return arr


if __name__ == '__main__':
    arr = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8]
    n = len(arr)
    assert rearrange(arr, n) == [4, 2, 12, 8, 0, 0, 0, 0, 0, 0]

    arr = [2, 2, 0, 4, 0, 8]
    n = len(arr)
    assert rearrange(arr, n) == [4, 4, 8, 0, 0, 0]
