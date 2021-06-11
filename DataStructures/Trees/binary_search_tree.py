"""
Binary search tree operations

Operation  |  Best Case  |  Average Case  |  Worst Case
Search     |  O(log n)   |  O(log n)      |  O(n)
Insertion  |  O(log n)   |  O(log n)      |  O(n)
Deletion   |  O(log n)   |  O(log n)      |  O(n)

Space complexity for all opertaions is O(n).
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def inorder(root):
    if root is not None:
        inorder(root.left_child)
        print(str(root.data) + " ->", end=" ")
        inorder(root.right_child)


def insert(node, data):
    if node is None:
        return Node(data)

    if data < node.data:
        node.left_child = insert(node.left_child, data)
    else:
        node.right_child = insert(node.right_child, data)

    return node


def minimum_value_node(node):
    current = node
    while current.left_child:
        current = current.left_child

    return current


def delete_node(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left_child = delete_node(root.left_child, data)
    elif data > root.data:
        root.right_child = delete_node(root.right_child, data)
    else:
        if root.left_child is None:
            temp = root.right_child
            root = None
            return temp
        elif root.right_child is None:
            temp = root.left_child
            root = None
            return temp

        temp = minimum_value_node(root.right_child)
        root.data = temp.data
        root.right_child = delete_node(root.right_child, temp.data)

    return root


if __name__ == "__main__":
    root = None
    root = insert(root, 8)
    root = insert(root, 3)
    root = insert(root, 1)
    root = insert(root, 6)
    root = insert(root, 7)
    root = insert(root, 10)
    root = insert(root, 14)
    root = insert(root, 4)

    print("Inorder traversal: ", end=" ")
    inorder(root)
    print("\nDelete 10")
    root = delete_node(root, 10)
    print("Inorder traversal: ", end=" ")
    inorder(root)
