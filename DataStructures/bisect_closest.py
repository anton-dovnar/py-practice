"""
We can use bisect to find the closest element
to what we are looking for very quickly.
"""
import bisect
import random


def find_closest(haystack, needle):
    # bisect.bisect_left will return the first value in the haystack
    # that is greater than needle
    i = bisect.bisect_left(haystack, needle)
    if i == len(haystack):
        return i - 1
    elif haystack[i] == needle:
        return i
    elif i > 0:
        j = i - 1
        # since we know the value is larger than needle (and vice versa for the
        # value at j), we don't need to use absolute values here
        if haystack[j] - needle > needle - haystack[j]:
            return j

    return i


if __name__ == '__main__':
    numbers = []

    for i in range(10):
        new_number = random.randint(0, 1000)
        bisect.insort(numbers, new_number)

    print(numbers)

    closest_index = find_closest(numbers, -250)
    print(f'Closest value to -250: {numbers[closest_index]}')

    closest_index = find_closest(numbers, 500)
    print(f'Closest value to 500: {numbers[closest_index]}')

    closest_index = find_closest(numbers, 1100)
    print(f'Closest value to 1100: {numbers[closest_index]}')
