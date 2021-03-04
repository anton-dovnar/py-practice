from collections import deque


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def gen_fib(n):
    for x in range(1, n + 1):
        yield fib(x)


if __name__ == '__main__':
    tasks = [gen_fib(3), gen_fib(5)]
    queue = deque()
    queue.extend(tasks)

    while queue:
        try:
            tasks = queue.popleft()
            print(next(tasks))
            queue.append(tasks)
        except StopIteration:
            print('Tasks done')
