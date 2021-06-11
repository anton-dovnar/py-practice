"""
AVL tree is a self-balancing binary search tree in which each node maintains
extra information called a balance factor whose value is either -1, 0 or +1.

AVL Tree Applications:
    - For indexing large records in databases
    - For searching in large databases

Time complexity of Insertion / Deletion / Search: O(log n)
"""
import sys


class Node:

    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.height = 1


class AVLTree:

    def insert_node(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left_child = self.insert_node(root.left_child, key)
        else:
            root.right_child = self.insert_node(root.right_child, key)

        root.height = 1 + max(self.get_height(root.left_child), self.get_height(root.right_child))
        balance_factor = self.get_balance_factor(root)
        if balance_factor > 1:
            if key < root.left_key:
                return self.right_rotate(root)
            else:
                root.left_child = self.left_rotate(root.left_child)
                return self.right_rotate(root)

        if balance_factor < -1:
            if key > root.right_child.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right_child)
                return self.left_rotate(root)

        return root

    def delete_node(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left_child = self.delete_node(root.left_child, key)
        elif key > root.key:
            root.right_child = self.delete_node(root.right_child, key)
        else:
            if root.left_child is None:
                temp = root.right_child
                root = None
                return temp
            elif root.right_child is None:
                temp = root.left_child
                root = None
                return temp

        temp = self.get_minimum_value_node(root.right_child)
        root.key = temp.key
        root.right_child = self.delete_node(root.right_child, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left_child), self.get_height(root.right_child))
        balance_factor = self.get_balance_factor(root)

        if balance_factor > 1:
            if self.get_balance_factor(root.left_child) >= 0:
                return self.right_rotate(root)
            else:
                root.left_child = self.left_rotate(root.left_child)
                return self.right_rotate(root)
        if balance_factor < -1:
            if self.get_balance(root.right_child) <= 0:
                return self.left_rotate(root)
            else:
                root.right_child = self.right_rotate(root.right_child)
                return self.left_rotate(root)
        return root

    def left_rotate(self, z):
        y = z.right_child
        T2 = y.left_child
        y.left_child = z
        z.right_child = T2
        z.height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        return y

    def right_rotate(self, z):
        y = z.left_child
        T3 = y.right_child
        y.right_child = z
        z.left_child = T3
        z.height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance_factor(self, root):
        if not root:
            return 0
        return self.get_height(root.left_child) - self.get_height(root.right_child)

    def get_minimum_value_node(self, root):
        if not root or not root.left_child:
            return root
        return self.get_minimum_value_node(root.left_child)

    def preorder(self, root):
        if not root:
            return
        print(f"{root.key}", end="")
        self.preorder(root.left_child)
        self.preorder(root.right_child)

    def print_tree(self, current, indent, last):
        if current:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "    "
            else:
                sys.stdout.write("L----")
                indent += "|   "
            print(current.key)
            self.print_tree(current.left_child, indent, False)
            self.print_tree(current.right_child, indent, True)


if __name__ == "__main__":
    tree = AVLTree()
    root = None
    numbers = [33, 13, 52, 9, 21, 61, 8, 11]
    for number in numbers:
        root = tree.insert_node(root, number)

    tree.print_tree(root, "", True)
    key = 13
    root = tree.delete_node(root, key)
    print("After Delettion: ")
    tree.print_tree(root, "", True)
