"""
Treap - Tree + Heap
Randomized Search Tree

Average-case time complexity: O(log n)
Worst-case scenario: O(n)
"""
from random import randrange


class Node:
    def __init__(self, key: int, priority=100, left=None, right=None) -> None:
        self.key = key
        self.priority = randrange(priority)
        self.left = left
        self.right = right


class Treap:
    def __init__(self, root=None) -> None:
        self.root = root

    def left_rotation(self, node):
        """
        Function to left-rotate a given treap

          r                       R
         / \     Left Rotate     / \
        L   R       ———>        r   Y
           / \                     / \
          X   Y                   L   X
        """

        R = node.right
        X = node.right.left
        R.left = node
        node.right = X
        return R

    def right_rotation(self, node):
        """
        Function to right-rotate a given treap

            r                        L
           / \     Right Rotate     / \
          L   R       ———>         X   r
         / \                          / \
        X   Y                        Y   R
        """

        L = node.left
        Y = node.left.right
        L.right = node
        node.left = Y
        return L

    def insert_node(self, pointer, key):
        if not pointer:
            return Node(key)

        # if the given data is less than the root node, insert in the left subtree;
        # otherwise, insert in the right subtree
        if key < pointer.key:
            pointer.left = self.insert_node(pointer.left, key)
            if pointer.left and pointer.left.priority > pointer.priority:
                pointer = self.right_rotation(pointer)
        else:
            pointer.right = self.insert_node(pointer.right, key)
            if pointer.right and pointer.right.priority > pointer.priority:
                pointer = self.left_rotation(pointer)

        return pointer

    def search_node(self, pointer, key):
        """
        Recursive function to search for a key in a given treap
        """
        if not pointer:
            return False

        if pointer.key == key:
            return True

        if key < pointer.key:
            return self.search_node(pointer.left, key)
        return self.search_node(pointer.right, key)

    def delete_node(self, pointer, key):
        """
        Recursive function to delete a key from a given treap
        """
        if not pointer:
            return None

        if key < pointer.key:
            pointer.left = self.delete_node(pointer.left, key)
        elif key > pointer.key:
            pointer.right = self.delete_node(pointer.right, key)
        else:
            # Case 1: node to be deleted has no children (it is a leaf node)
            if not pointer.left and not pointer.right:
                pointer = None
            # Case 2: node to be deleted has two children
            elif pointer.left and pointer.right:
                if pointer.left.priority < pointer.right.priority:
                    pointer = self.left_rotation(pointer)
                    pointer.left = self.delete_node(pointer.left, key)
                else:
                    pointer = self.right_rotation(pointer)
                    pointer.right = self.delete_node(pointer.right, key)
            # Case 3: node to be deleted has only one child
            else:
                child = pointer.left if pointer.left else pointer.right
                pointer = child

        return pointer


def print_treap(root, space):
    """
    Utility function to print two-dimensional view of a treap using
    """
    if not root:
        return

    height = 10
    space += height
    print_treap(root.right, space)
    for _ in range(height, space):
        print(' ', end='')
    print((root.key, root.priority))
    print_treap(root.left, space)


if __name__ == '__main__':
    # Treap keys
    keys = [5, 2, 1, 4, 9, 8, 10]

    # construct a treap
    root = Node(keys[0])
    treap = Treap(root)

    for key in keys[1:]:
        treap.insert_node(treap.root, key)

    print("Constructed :\n\n")
    print_treap(treap.root, 0)

    print("\nDeleting node 1:\n\n")
    treap.delete_node(treap.root, 1)
    print_treap(treap.root, 0)

    print("\nDeleting node 5:\n\n")
    treap.delete_node(treap.root, 5)
    print_treap(treap.root, 0)

    print("\nDeleting node 9:\n\n")
    treap.delete_node(treap.root, 9)
    print_treap(treap.root, 0)
