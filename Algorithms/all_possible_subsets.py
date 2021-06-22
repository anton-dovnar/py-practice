from typing import List


def possible_subsets(letters: List[int], length: int) -> None:
    for i in range(1 << length):
        for j in range(length):
            if i & (1 << j):
                print(letters[j], end=" ")
        print()


if __name__ == '__main__':
    unique_items = ['a', 'b', 'c']
    possible_subsets(unique_items, len(unique_items))
