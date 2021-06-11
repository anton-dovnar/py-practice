"""
Checking if a binary tree is a perfect binary tree.

A perfect binary tree is a type of binary tree in which every internal
node has exactly two child nodes and all the leaf nodes are at the same level.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def calculate_depth(node):
    depth = 0
    while node is not None:
        depth += 1
        node = node.left_child
    return depth


def is_perfect_tree(root, depth, level=0):
    if root is None:
        return True

    if root.left_child is None and root.right_child is None:
        return depth == level + 1

    if root.left_child is None or root.right_child is None:
        return False

    return (
        is_perfect_tree(root.left_child, depth, level + 1) and
        is_perfect_tree(root.right_child, depth, level + 1)
    )


if __name__ == "__main__":
    root = Node(1)
    root.left_child = Node(2)
    root.right_child = Node(3)
    root.left_child.left_child = Node(4)
    root.left_child.right_child = Node(5)
    root.right_child.left_child = Node(4)
    root.right_child.right_child = Node(5)

    if is_perfect_tree(root, calculate_depth(root)):
        print("The tree is a perfect binary tree")
    else:
        print("The tree is not a perfect binary tree")
