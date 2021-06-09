class Stack:
    def __init__(self):
        self.stack = []

    @property
    def is_empty(self) -> bool:
        return not self.stack

    def push(self, item):
        self.stack.append(item)
        print(f"pushed item: {item}")

    def pop(self):
        if self.is_empty:
            return "stack is empty"

        return self.stack.pop()

    def __str__(self):
        return str(self.stack)


if __name__ == '__main__':
    s = Stack()
    print("Check is empty:", s.is_empty)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s)
    print(f"popped item: {s.pop()}")
    print(s)
    print("Check is empty:", s.is_empty)
