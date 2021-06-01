"""
All elements at even positions in increasing order
All elements at odd positions in decreasing order

Time complexity: O(n)
Space complexity: O(n)
"""
import copy


def rearranger_arr(arr: list):
    n = len(arr)
    even_range = n // 2
    odd_range = n - even_range
    temp_arr = copy.deepcopy(arr)
    temp_arr.sort()

    j = odd_range - 1
    for i in range(0, n, 2):
        arr[i] = temp_arr[j]
        j = j - 1

    j = odd_range
    for i in range(1, n, 2):
        arr[i] = temp_arr[j]
        j = j + 1

    return arr


if __name__ == '__main__':
    arr = [1, 2, 1, 4, 5, 6, 8, 8]
    print(rearranger_arr(arr))
    assert rearranger_arr(arr) == [4, 5, 2, 6, 1, 8, 1, 8]

    arr = [1, 2, 3, 4, 5, 6, 7]
    print(rearranger_arr(arr))
    assert rearranger_arr(arr) == [4, 5, 3, 6, 2, 7, 1]
