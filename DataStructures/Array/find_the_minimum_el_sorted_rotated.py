"""
Find the minimum element in a sorted and rotated arr

Time complexity: O(log n)
"""


def find_min(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] == arr[right]:
            right -= 1
        elif arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return arr[right]


if __name__ == '__main__':
    arr1 = [5, 6, 1, 2, 3, 4]
    print("The minimum element is ", find_min(arr1))

    arr2 = [1, 2, 3, 4]
    print("The minimum element is ", find_min(arr2))

    arr3 = [1]
    print("The minimum element is ", find_min(arr3))

    arr4 = [1, 2]
    print("The minimum element is ", find_min(arr4))

    arr5 = [2, 1]
    print("The minimum element is ", find_min(arr5))

    arr6 = [5, 6, 7, 1, 2, 3, 4]
    print("The minimum element is ", find_min(arr6))
