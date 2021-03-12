from threading import Thread


def simple_sum(n):
    count = 0
    for i in range(n):
        count += i
        print(f'Simple sum computes: {count}')


def simple_square(n):
    count = 0
    for i in range(n):
        count += i * i
        print(f'Simple square computes: {count}')


def simple_cube(n):
    count = 0
    for i in range(n):
        count += i * i * i
        print(f'Simple cube computes: {count}')


if __name__ == '__main__':
    n = 10
    thread_sum = Thread(target=simple_sum, args=(n,))
    thread_square = Thread(target=simple_square, args=(n,))
    thread_cube = Thread(target=simple_cube, args=(n,))

    # Start execution
    thread_sum.start()
    thread_square.start()
    thread_cube.start()

    # Wait until thread terminates
    thread_sum.join()
    thread_square.join()
    thread_cube.join()
