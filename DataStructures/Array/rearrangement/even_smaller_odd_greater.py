"""
Rearrange array such that even index elements are smaller and odd
index elements are greater

Time complexity: O(n)
Space complexity: O(1)
"""


def rearrange(arr: list) -> list:
    for i in range(len(arr) - 1):
        if i % 2 == 0 and arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if i % 2 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


if __name__ == '__main__':
    arr = [6, 4, 2, 1, 8, 3]
    print(rearrange(arr))
