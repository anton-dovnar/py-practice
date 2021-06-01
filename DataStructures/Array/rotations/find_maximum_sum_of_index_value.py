"""
Find maximum value of Sum(i*arr[i])
with only rotations on given array

Time complexity: O(n)
Space complexity: O(1)
"""


def max_sum(arr):
    arr_sum = 0  # arr[i]
    curr_val = 0  # i * arr[i]
    n = len(arr)

    for i in range(n):
        arr_sum += arr[i]
        curr_val += i * arr[i]

    max_val = curr_val

    # try all rotations one by one and find the maximum rotaion sum
    for j in range(1, n):
        curr_val += arr_sum - n * arr[n - j]
        if curr_val > max_val:
            max_val = curr_val

    return max_val


if __name__ == '__main__':
    arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Max sum is:", max_sum(arr))
