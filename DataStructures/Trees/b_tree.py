"""
B tRee Applications:
    - databases and file systems
    - to store blocks of data (secondary storage media)
    - multilevel indexing

Searching Complexity on B Tree:
    Time complexity: O(log n)
    Space complexity: O(n)
"""


class Node:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, degree):
        self.root = Node(True)
        self.degree = degree

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.degree) - 1:
            temp = Node()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.degree) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.degree
        y = x.child[i]
        z = Node(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    def print_tree(self, x, level=0):
        print("Level ", level, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        level += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, level)


if __name__ == "__main__":
    b_tree = BTree(3)
    for i in range(10):
        b_tree.insert((i, 2 * i))

    b_tree.print_tree(b_tree.root)
