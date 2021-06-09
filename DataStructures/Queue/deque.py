"""
Applications of Deque Data Structure:
    In undo operations on software.
    To store history in browsers.
    For implementing both stacks and queues.
"""


class Deque:

    def __init__(self):
        self.deque = []

    @property
    def is_empty(self) -> bool:
        return not self.deque

    def add_rear(self, item):
        self.deque.append(item)

    def add_front(self, item):
        self.deque.insert(0, item)

    @property
    def remove_front(self):
        return self.deque.pop(0)

    @property
    def remove_rear(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)


if __name__ == '__main__':
    d = Deque()
    print("Is empty:", d.is_empty)
    d.add_rear(8)
    d.add_rear(5)
    d.add_front(7)
    d.add_front(10)
    print("Length of deque", len(d))
    print("Is empty:", d.is_empty)
    d.add_rear(11)
    print("Remove rear", d.remove_rear)
    print("Remove front", d.remove_front)
    d.add_front(55)
    d.add_rear(45)
    print(d.deque)
