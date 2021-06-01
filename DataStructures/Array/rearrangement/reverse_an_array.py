"""
Write a program to reverse and array or string

Time complexity: O(n)
Space complexity: O(1)
"""


def reverse_arr(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    print(reverse_arr(arr))
