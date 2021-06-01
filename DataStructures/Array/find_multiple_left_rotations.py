"""
Quickly find multiple left rotations of an array
"""


def left_rotate(arr, n, k):
    for i in range(k, k + n):
        print(arr[i % n], end=" ")


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    n = len(arr)
    k = 2
    left_rotate(arr, n, k)
    print()

    k = 3
    left_rotate(arr, n, k)
    print()

    k = 4
    left_rotate(arr, n, k)
    print()
