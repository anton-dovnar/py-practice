"""
Closure function / class definition
"""


def closure():
    x = 1

    def inner_func():
        nonlocal x
        x += 1
        return x
    return inner_func


class Closure:
    """ Closure class vesrion """

    def __init__(self):
        self._x = 1

    def __call__(self):
        self._x += 1
        return self._x


if __name__ == '__main__':
    cs = closure()
    print(f'{cs} - definition output:')
    for _ in range(3):
        print(cs())

    cs_cls = Closure()
    print(f'\n{cs_cls} definition output:')
    for _ in range(3):
        print(cs_cls())
