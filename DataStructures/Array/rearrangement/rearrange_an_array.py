"""
Rearrange an array such that arr[i] = i

Time complexity: O(n)
Space complexity: O(1)
"""


def fix(arr):
    for i in range(len(arr)):
        if arr[i] != -1 and arr[i] != i:
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
    return arr


if __name__ == "__main__":
    arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    print(fix(arr))

    arr = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
    print(fix(arr))
