"""
::rotate:: number of elements to rotate
::length:: length of the array
Number of sets is equal to `gcd(rotate, length)`

Time complexity: O(n)
Space complexity: O(1)
"""
import math


def left_rotate(arr, rotate, length):
    rt = rotate % length
    if rt == 0:
        return arr
    gcd = math.gcd(rt, length)
    for i in range(gcd):
        temp = arr[i]
        j = i
        while True:
            k = j + rt
            if k >= length:
                k -= length
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
    return arr


if __name__ == '__main__':
    print(left_rotate([1, 2, 3, 4, 5, 6, 7], 2, 7))
