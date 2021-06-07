"""
Linked list does not support binary search.
Skip list allows fast search and insertion.
The number of layers should be log n.

Average case:
    Search: O(log n)
    Insertion: O(log n)
"""
import random


class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)


class SkipList:
    def __init__(self, max_lvl, p):
        self.max_lvl = max_lvl
        self.p = p  # p is the fraction of the nodes with level

        # create header node and initialize key to -1
        self.header = self.create_node(self.max_lvl, -1)
        # current level of skip list
        self.level = 0

    def create_node(self, lvl, key):
        n = Node(key, lvl)
        return n

    def random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_lvl:
            lvl += 1
        return lvl

    def insert_element(self, key):
        # create update array and initialize it
        update = [None] * (self.max_lvl + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current is None or current.key != key:
            rlevel = self.random_level()

            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                self.level = rlevel

            # create new node with random level generated
            n = self.create_node(rlevel, key)

            # insert node by rearranging references
            for i in range(rlevel + 1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n

            print("Successfully inserted key {}".format(key))

    # Display skip list level wise
    def display_list(self):
        print("\n*****Skip List******")
        head = self.header
        for lvl in range(self.level + 1):
            print("Level {}: ".format(lvl), end=" ")
            node = head.forward[lvl]
            while node is not None:
                print(node.key, end=" ")
                node = node.forward[lvl]
            print("")


if __name__ == '__main__':
    lst = SkipList(3, 0.5)
    lst.insert_element(3)
    lst.insert_element(6)
    lst.insert_element(7)
    lst.insert_element(9)
    lst.insert_element(12)
    lst.insert_element(19)
    lst.insert_element(17)
    lst.insert_element(26)
    lst.insert_element(21)
    lst.insert_element(25)
    lst.display_list()
