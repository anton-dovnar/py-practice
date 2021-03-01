"""
Linked lists are a sequential collection of data that uses relational pointers
on each data node to link to the next node in the list.
Unlike arrays, linked lists do not have objective positions in the list.
Instead, they have relational positions based on their surrounding nodes.
The first node in a linked list is called the head node, and the final is
called the tail node, which has a null pointer.
"""


class Node:

    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None


class SLinkedList:

    def __init__(self):
        self.head_val = None


if __name__ == '__main__':
    list1 = SLinkedList()
    list1.head_val = Node('Mon')
    e2 = Node('Tue')
    e3 = Node('Wed')

    # Link first Node to second node
    list1.head_val.next_val = e2

    # Link second Node to third node
    e2.next_val = e3
