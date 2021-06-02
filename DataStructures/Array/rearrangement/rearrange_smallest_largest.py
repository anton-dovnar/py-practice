"""
Rearrange an array in order - smallest, largest,
2nd smallest, 2nd largest, ...

Time complexity: O(n log n)
Space complexity: O(n)
"""


def rearrange(arr: list, n: int):
    arr.sort()
    temp_arr = [0] * (n + 1)
    arr_idx = 0

    i = 0
    j = n - 1
    mid = n // 2 if n % 2 else n // 2 - 1
    while i <= mid or j > mid:
        temp_arr[arr_idx] = arr[i]
        arr_idx += 1
        temp_arr[arr_idx] = arr[j]
        arr_idx += 1
        i += 1
        j -= 1

    for i in range(n):
        arr[i] = temp_arr[i]

    return arr


if __name__ == '__main__':
    arr = [5, 8, 1, 4, 2, 9, 3, 7, 6]
    n = len(arr)
    print(rearrange(arr, n))

    arr1 = [1, 2, 3, 4]
    n = len(arr1)
    print(rearrange(arr1, n))
