"""
Python program to find number of pairs with a given sum in a sorted and rotated array.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def pairs_in_sorted_rotated(arr, n, x):
    # Find the pivot element.
    for i in range(n):
        if arr[i] > arr[i + 1]:
            break

    left = (i + 1) % n  # index of smallest element
    right = i  # index of largest element
    counter = 0  # count pairs of given sum

    while left != right:
        if arr[left] + arr[right] == x:
            print('Found pairs:', arr[left], arr[right])
            counter += 1

            if left == (right - 1 + n) % n:
                return counter

            left = (left + 1) % n
            right = (right - 1 + n) % n

        elif arr[left] + arr[right] < x:
            left = (left + 1) % n
        else:
            right = (n + right - 1) % n

    return counter


if __name__ == '__main__':
    arr = [11, 15, 6, 7, 9, 10]
    s = 16
    print(pairs_in_sorted_rotated(arr, 6, s))
