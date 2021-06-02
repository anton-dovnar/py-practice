"""
Find the minumu number of swaps required to bring all the numbers
less than or equal to k together.

::good:: elements which less than or equl to k
::bad:: elements which greater than k

Time complexity: O(n)
Space complexity: O(1)
"""


def min_swap(arr, n, k):
    good = 0
    for i in range(n):
        if arr[i] <= k:
            good += 1

    bad = 0
    for i in range(good):
        if arr[i] > k:
            bad += 1

    ans = bad
    for i in range(good, n):
        if arr[i] > k:
            bad += 1

        if arr[i - good] > k:
            bad -= 1

        ans = min(ans, bad)

    return ans


if __name__ == '__main__':
    arr = [2, 1, 5, 6, 3]
    n = len(arr)
    k = 3
    print(min_swap(arr, n, k))

    arr1 = [2, 7, 9, 5, 8, 7, 4]
    n = len(arr1)
    k = 5
    print(min_swap(arr1, n, k))
