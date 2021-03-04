"""
Define context manager class
Context manager accepts two dunder methods it is __enter__
and __exit__
"""
from functools import wraps
from contextlib import contextmanager


class GeneratorCM:

    def __init__(self, gen):
        self._gen = gen

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, *exc_info):
        try:
            if exc_info[0] is None:
                next(self._gen)
            else:
                self._gen.throw(*exc_info)
            raise RuntimeError
        except StopIteration:
            return True


# Define a decorator
def context_manager(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return GeneratorCM(func(*args, **kwargs))
    return wrapper


def my_list():
    try:
        yield [1, 2, 3, 4, 5]
    finally:
        print('exit scope')


if __name__ == '__main__':
    custom_ctx = context_manager(my_list)
    print('Custom context manager:')
    with custom_ctx() as ml:
        print(ml)

    default_ctx = contextmanager(my_list)
    print('\nInternal contextlib.contextmanager:')
    with default_ctx() as ml:
        print(ml)
