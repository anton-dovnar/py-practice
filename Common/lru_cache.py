import timeit


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


default_timer = timeit.timeit('fibonacci(15)', 'from __main__ import fibonacci', number=10000)
print(f'Total time: {default_timer:.3f}')


test_with_cache = '''
@lru_cache
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)
'''


cache_timer = timeit.timeit(test_with_cache, 'from functools import lru_cache', number=10000)
print(f'Total time with cache: {cache_timer:.3f}')
