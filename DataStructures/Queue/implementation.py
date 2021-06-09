"""
FIFO - First In First Out

Applications of Queue:
    CPU scheduling, Disk Scheduling
    Call Center phone systems use Queues to hold people calling them in order.
"""


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q)
    q.dequeue()
    print("After removing an element", q)
    print("Size of queue:", len(q))
