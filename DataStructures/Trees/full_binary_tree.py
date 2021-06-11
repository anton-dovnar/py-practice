"""
Checking if a binary tree is a full binary tree
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def is_full_tree(root) -> bool:
    if root is None:
        return True

    if root.left_child is None and root.right_child is None:
        return True

    if root.left_child and root.right_child:
        return (is_full_tree(root.left_child) and is_full_tree(root.right_child))

    return False


if __name__ == "__main__":
    root = Node(1)
    root.left_child = Node(2)
    root.right_child = Node(3)

    root.left_child.left_child = Node(4)
    root.left_child.right_child = Node(5)
    root.left_child.right_child.left_child = Node(6)
    root.left_child.right_child.right_child = Node(7)

    if is_full_tree(root):
        print("The tree is a full binary tree")
    else:
        print("The tree is not a full binary tree")
