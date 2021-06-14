"""
Time copmlexity: O(n log n)
"""
from random import randint
from timer import run_sorting_algorithm


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [number for number in arr[1:] if number <= pivot]
        greater = [number for number in arr[1:] if number > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    array = [randint(0, 1000) for _ in range(1000)]
    run_sorting_algorithm(algorithm="quick_sort", array=array)
