"""
Find element at given index after a number of rotations
"""


def find_element(arr, ranges, rotations, index):
    for i in range(rotations - 1, -1, -1):
        left = ranges[i][0]
        right = ranges[i][1]
        if left <= index and right >= index:
            if index == left:
                index = right
            else :
                index -= 1

    return arr[index]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    rotations = 2
    ranges = [[0, 2], [1, 4], [0, 3]]
    index = 1
    print(find_element(arr, ranges, rotations, index))
