"""
Fibonacci Heap Applications
Complexities:
    Insertion: O(1)
    Find Min: O(1)
    Union: O(1)
    Extract Min: O(log n)
    Decrease Key: O(1)
    Delete Node: O(log n)
"""
import math


class FibonacciTree:
    """Fibonacci tree"""

    def __init__(self, value):
        self.value = value
        self.child = []
        self.order = 0

    def add_at_end(self, t):
        """Adding tree at the end of the tree"""

        self.child.append(t)
        self.order += 1


class FibonacciHeap:
    """Fibonacci heap"""

    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0

    def insert_node(self, value):
        """Insert a node"""

        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        if self.least is None or value < self.least.value:
            self.least = new_tree
        self.count += 1

    @property
    def get_min(self):
        """Get minimum value"""

        if self.least is None:
            return None
        return self.least.value

    def extract_min(self):
        """Extract the minimum value"""

        smallest = self.least
        if smallest is not None:
            for child in smallest.child:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count -= 1
            return smallest.value

    def consolidate(self):
        """Consolidate the tree"""

        aux = (floor_log(self.count) + 1) * [None]

        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order += 1
            aux[order] = x

        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if self.least is None or k.value < self.least.value:
                    self.least = k


def floor_log(x):
    return math.frexp(x)[1] - 1


if __name__ == '__main__':
    fibonacci_heap = FibonacciHeap()
    fibonacci_heap.insert_node(7)
    fibonacci_heap.insert_node(3)
    fibonacci_heap.insert_node(17)
    fibonacci_heap.insert_node(24)
    print('The minimum value of the fibonacci heap: {}'.format(fibonacci_heap.get_min))
    print('The minimum value removed: {}'.format(fibonacci_heap.extract_min()))
