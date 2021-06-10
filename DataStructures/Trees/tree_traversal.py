"""
Tree Traversal - preorder, inorder and postorder
"""


class Node:

    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def preorder(root):
    """VLR Technique"""

    if root:
        print(str(root.val) + "->", end="")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    """LVR Technique"""

    if root:
        inorder(root.left)
        print(str(root.val) + "->", end="")
        inorder(root.right)


def postorder(root):
    """LRV Technique"""

    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end="")


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("\nPreorder traversal ")
    preorder(root)

    print("\nInorder traversal ")
    inorder(root)

    print("\nPostorder traversal ")
    postorder(root)
