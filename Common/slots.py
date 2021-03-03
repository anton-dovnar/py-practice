import resource
import platform
from functools import wraps


def profile_mem(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        ret = func(*args, **kwargs)
        e = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        uname = platform.system()
        if uname == "Linux":
            print(f"mem usage: {e - s} kByte")

        return ret
    return wrapper


class A:
    __slots__ = ['attr1', 'attr2', 'attr3']

    def __init__(self):
        self.attr1 = 'Foo'
        self.attr2 = 'Bar'
        self.attr3 = 'Baz'


class B:

    def __init__(self):
        self.attr1 = 'Foo'
        self.attr2 = 'Bar'
        self.attr3 = 'Baz'


@profile_mem
def alloc(cls):
    _ = [cls() for _ in range(1000000)]


if __name__ == '__main__':
    alloc(A)
    alloc(B)
