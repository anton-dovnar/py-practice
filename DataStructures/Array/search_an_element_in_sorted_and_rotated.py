"""
Time complexity: O(log n)
Space complexity: O(1)
"""


def search(arr, key):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        left_val = arr[left]
        right_val = arr[right]
        mid_val = arr[mid]

        if mid_val == key:
            return mid

        if mid_val <= left_val:
            if mid_val < key <= right_val:
                left = mid + 1
            else:
                right = mid - 1

        if mid_val >= left_val:
            if left_val <= key < mid_val:
                right = mid - 1
            else:
                left = mid + 1

    if arr[left] == key:
        return left
    return - 1


if __name__ == '__main__':
    arr = [4, 5, 6, 7, 0, 1, 2]
    key = 7
    print(search(arr, key))
