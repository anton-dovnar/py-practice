"""
Checking if a binary tree is balanced binary tree

A balanced binary tree, aslo referred to as a height-balanced binary tree, is
defined as a binary tree in which the height of the left and right subtree of
any node differ by not more than 1.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class CalculateHeight:

    def __init__(self):
        self.height = 0


def is_height_balanced(root, calculate_height):
    left = CalculateHeight()
    right = CalculateHeight()

    if root is None:
        return True

    left_side = is_height_balanced(root.left_child, left)
    right_side = is_height_balanced(root.right_child, right)

    calculate_height.height = max(left.height, right.height) + 1

    if abs(left.height - right.height) <= 1:
        return left_side and right_side

    return False


if __name__ == "__main__":
    root = Node(1)
    root.left_child = Node(2)
    root.right_child = Node(3)
    root.left_child.left_child = Node(4)
    root.left_child.right_child = Node(5)

    calculate_height = CalculateHeight()
    if is_height_balanced(root, calculate_height):
        print("The tree is balanced")
    else:
        print("The tree is not balanced")
