"""
Time copmlexity: O(n^2)
"""
from random import randint
from timer import run_sorting_algorithm


def find_smallest(arr: list) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:
    new_arr = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


if __name__ == "__main__":
    array = [randint(0, 1000) for _ in range(1000)]
    run_sorting_algorithm(algorithm="selection_sort", array=array)
