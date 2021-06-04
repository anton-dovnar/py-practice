"""
Segregate even and odd numbers

Given an array of integers, segregate even and odd numbers in the array.
All the even numbers should be present first, and then the odd numbers.

Time complexity: O(n)
Space complexity: O(1)
"""


def rearrange(arr: list) -> list:
    count = 0  # Count even numbers
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
    return arr


if __name__ == '__main__':
    arr = [1, 9, 5, 3, 2, 6, 7, 11]
    print(rearrange(arr))

    arr = [1, 3, 2, 4, 7, 6, 9, 10]
    print(rearrange(arr))
