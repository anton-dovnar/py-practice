"""
We can find the majority element using linear time and constant space
using the Boyer-Moore majority vote algorithm.
"""
from typing import List


def find_majority(sequence: List[int]):
    majority_element = -1
    i = 0

    for _, value in enumerate(sequence):
        if i == 0:
            majority_element = value
            i = 1
        elif majority_element == value:
            i += 1
        else:
            i -= 1

    return majority_element


if __name__ == "__main__":
    sequence = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]
    print("The majority element is", find_majority(sequence))
