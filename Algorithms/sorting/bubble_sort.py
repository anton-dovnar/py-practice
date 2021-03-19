from random import randint
from timer import run_sorting_algorithm


def bubble_sort(array):
    size = len(array)

    for i in range(size):
        already_sorted = True

        for j in range(size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array


if __name__ == "__main__":
    array = [randint(0, 1000) for _ in range(1000)]
    run_sorting_algorithm(algorithm="bubble_sort", array=array)
