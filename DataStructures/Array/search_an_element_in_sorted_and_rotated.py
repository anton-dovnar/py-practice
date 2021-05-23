"""
Time complexity: O(log n)
Space complexity: O(1)
"""


def search(arr, start, end, key):
    if start > end:
        return -1

    mid = (start + end) // 2
    if arr[mid] == key:
        return mid

    if arr[start] <= arr[mid]:
        if arr[start] <= key <= arr[mid]:
            return search(arr, start, mid - 1, key)
        return search(arr, mid + 1, end, key)

    if arr[mid] <= key <= arr[end]:
        return search(arr, mid + 1, end, key)
    return search(arr, start, mid - 1, key)


if __name__ == '__main__':
    arr = [4,5,6,7,0,1,2]
    key = 3
    start = 0
    end = len(arr) - 1
    print(search(arr, start, end, key))
