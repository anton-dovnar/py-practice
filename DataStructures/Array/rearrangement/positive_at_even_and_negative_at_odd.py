"""
Positive elements at even and negative at odd positions
(Relative order not maintained)

Time complexity: O(n log n)
Space complexity: O(1)
"""


def rearrange(arr: list) -> list:
    n = len(arr)
    arr.sort()
    j = n - 2 if n % 2 else n - 1

    for i in range(0, n // 2, 2):
        arr[i], arr[j] = arr[j], arr[i]
        j -= 2
    return arr


if __name__ == '__main__':
    arr = [1, -3, 5, 6, -3, 6, 7, -4, 9, 10]
    arr = [1, -3, 5, 6, -3, 6, 7, -4, 9, 10, -8]
    print(rearrange(arr))
