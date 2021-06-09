"""
Priority queue implementation time:
    Linked List: peek - O(1); insert - O(n); delete - O(1);
    Binary Heap: peek - O(1); insert - O(log n); delete - O(log n);
    Binary Search Tree: peek - O(1); insert - O(log n); delete - O(log n);

Priority Queue Applications:
    - Dijkstra's algorithm
    - for implementing stack
    - for load balancing and interrupt handling in an operating system
    - for data compression in Huffman code
"""


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert(array, new_num):
    size = len(array)
    if size == 0:
        array.append(new_num)
    else:
        array.append(new_num)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


def delete_node(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]
    array.remove(size - 1)

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array: " + str(arr))
delete_node(arr, 4)
print("After deleting an element: " + str(arr))
