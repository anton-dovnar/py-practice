"""
Rearrange positive and negative numbers

Time complexity: O(n)
Space complexity: O(1)
"""


def rearrange(arr, n):
    i = 0
    for j in range(n):
        if arr[j] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Now all positive numbers are at end and negative numbers
    # at the beginning of array. Initialize indexes for starting
    # point of positive and negative numbers to be swapped
    pos, neg = i, 0

    # Increment the negative index by 2 and positive index by 1,
    # i.e., swap every alternate negative number with next
    # positive number
    while pos < n and neg < pos and arr[neg] < 0:
        # swapping of arr
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2
    return arr


if __name__ == '__main__':
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    n = len(arr)
    print(rearrange(arr, n))

    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    assert rearrange(arr, n) == [4, -3, 5, -1, 6, -7, 2, 8, 9]
