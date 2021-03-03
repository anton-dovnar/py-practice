def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        b, a = a + b, b


def fibonnaci(n):
    yield from fib(n)


if __name__ == '__main__':
    for f in fibonnaci(10):
        print(f)
