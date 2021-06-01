"""
Print left rotation of arr
"""


def left_rotate(arr: list, k: int):
    n = len(arr)
    mod = k % n
    for i in range(n):
        print(arr[(mod + i) % n], end=" ")


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    k = 2
    left_rotate(arr, k)
    print()

    k = 3
    left_rotate(arr, k)
