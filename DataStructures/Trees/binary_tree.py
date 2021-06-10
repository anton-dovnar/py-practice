"""
Binary Tree
"""


class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def preorder(self):
        """Traverse preorder"""

        print(self.val, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        """Traverse inorder"""

        if self.left:
            self.left.inorder()
        print(self.val, end=" ")
        if self.right:
            self.right.inorder()

    def postorder(self):
        """Traverse postorder"""

        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.val, end=" ")


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    print("Pre order Traversal: ", end="")
    root.preorder()
    print("\nIn order Traversal: ", end="")
    root.inorder()
    print("\nPost order Traversal: ", end="")
    root.postorder()
