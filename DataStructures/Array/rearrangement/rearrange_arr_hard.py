"""
Rearrange an array such that ‘arr[j]’ becomes ‘i’ if ‘arr[i]’ is ‘j’ | Set 1

Given an array of size n where all elements are distinct and in range from 0
to n-1, change contents of arr[] so that arr[i] = j is changed to arr[j] = i.

Time complexity: O(n)
Space complexity: O(n)
"""


def rearrange(arr: list):
    temp = [0] * len(arr)
    for i in range(len(arr)):
        temp[arr[i]] = i
    return temp


if __name__ == '__main__':
    arr = [1, 3, 0, 2]
    print(rearrange(arr))
    assert rearrange(arr) == [2, 0, 3, 1]

    arr = [2, 0, 1, 4, 5, 3]
    print(rearrange(arr))
    assert rearrange(arr) == [1, 2, 0, 5, 3, 4]

    arr = [0, 1, 2, 3]
    print(rearrange(arr))
    assert rearrange(arr) == [0, 1, 2, 3]
