"""
Applications of Circular Queue:
    Traffic Management
    Memory Management
"""


class CircularQueue:

    def __init__(self, n):
        self.n = n
        self.queue = [None] * n
        self.head = self.tail = -1

    def enqueue(self, data):
        if (self.tail + 1) % self.n == self.head:
            print("The circular queue is full")
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.n
            self.queue[self.tail] = data

    @property
    def dequeue(self):
        if self.head == -1:
            print("The circular queue is empty\n")
        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.n
            return temp

    @property
    def display(self):
        if self.head == -1:
            print("No element in the circular queue")
        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.n):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


if __name__ == "__main__":
    c = CircularQueue(6)
    for i in range(1, 7):
        c.enqueue(i)
    print("Initial queue")
    c.display
    c.dequeue
    print("After removing an element from the queue")
    c.display
