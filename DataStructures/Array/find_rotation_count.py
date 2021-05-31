"""
Find the Rotation Count in Rotated Sorted array

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def count_rotations(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if left > right:
            return 0
        elif right == left:
            return left
        elif mid < right and arr[mid] > arr[mid + 1]:
            return mid + 1
        elif mid > left and arr[mid] < arr[mid - 1]:
            return mid
        elif arr[right] > arr[mid]:
            right = mid - 1
        else:
            left = mid + 1


if __name__ == '__main__':
    arr = [11, 12, 15, 18, 2, 3, 6, 7]
    print(count_rotations(arr))
