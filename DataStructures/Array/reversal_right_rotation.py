"""
Reversal algorithm for right rotation of an array
"""


def reverse_arr(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def right_rotate(arr, k):
    n = len(arr) - 1
    reverse_arr(arr, 0, n)
    reverse_arr(arr, 0, k - 1)
    reverse_arr(arr, k, n)
    return arr


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    print(right_rotate(arr, k))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 4
    print(right_rotate(arr, k))
