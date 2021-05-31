def sum_pairs(arr, s):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] > s:
            right -= 1
        elif arr[left] + arr[right] < s:
            left += 1
        else:
            print(arr[left], arr[right])
            left += 1
            right -= 1


if __name__ == '__main__':
    arr = [11, 15, 6, 7, 9, 10]
    s = 16
    print(f'Pairs with sum equal to: {s}')
    sum_pairs(arr, s)
