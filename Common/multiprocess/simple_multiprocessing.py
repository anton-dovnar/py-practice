from multiprocessing import Process


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
    process_sum = Process(target=simple_sum, args=(n,))
    process_square = Process(target=simple_square, args=(n,))
    process_cube = Process(target=simple_cube, args=(n,))

    # Execute
    process_sum.start()
    process_square.start()
    process_cube.start()

    process_sum.join()
    process_square.join()
    process_cube.join()
