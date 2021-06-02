"""
Rearrange array such that even positioned are greater than odd

Time complexity: O(n)
Space complexity: O(1)
"""


def rearrange(arr: list, n: int):
    for i in range(1, n):
        if i % 2:  # Odd
            if arr[i] < arr[i - 1]:
                arr[i - 1], arr[i] = arr[i] , arr[i - 1]
        else:  # Even
            if arr[i] > arr[i - 1]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

    return arr


if __name__ == '__main__':
    arr = [1, 3, 2, 2, 5]
    n = len(arr)
    print(rearrange(arr, n))

    arr1 = [1, 2, 2, 1]
    n = len(arr1)
    print(rearrange(arr1, n))
