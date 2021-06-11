"""
Checking if a binary tree is a complete binary tree

A complete binary tree is a binary tree in which all the levels are
copmpletely filled except possibly the lowest one, which is filled from
the left.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def count_nodes(root):
    if root is None:
        return 0
    return (1 + count_nodes(root.left_child) + count_nodes(root.right_child))


def is_complete_tree(root, index, number_of_nodes):
    if root is None:
        return True

    if index >= number_of_nodes:
        return False
    return (
        is_complete_tree(root.left_child, 2 * index + 1, number_of_nodes) and
        is_complete_tree(root.right_child, 2 * index + 2, number_of_nodes)
    )


if __name__ == "__main__":
    root = Node(1)
    root.left_child = Node(2)
    root.right_child = Node(3)
    root.left_child.left_child = Node(4)
    root.left_child.right_child = Node(5)
    root.right_child.left_child = Node(6)

    node_count = count_nodes(root)
    index = 0

    if is_complete_tree(root, index, node_count):
        print("The tree is a copmlete binary tree")
    else:
        print("The tree is not a complete binary tree")
