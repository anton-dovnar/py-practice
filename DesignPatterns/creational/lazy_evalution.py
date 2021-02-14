"""
Lazily-evaluated property pattern in Python.

*References:
bottle
https://github.com/bottlepy/bottle/blob/cafc15419cbb4a6cb748e6ecdccf92893bb25ce5/bottle.py#L270
django
https://github.com/django/django/blob/ffd18732f3ee9e6f0374aff9ccf350d85187fac2/django/utils/functional.py#L19
pip
https://github.com/pypa/pip/blob/cb75cca785629e15efb46c35903827b3eae13481/pip/utils/__init__.py#L821
pyramid
https://github.com/Pylons/pyramid/blob/7909e9503cdfc6f6e84d2c7ace1d3c03ca1d8b73/pyramid/decorator.py#L4
werkzeug
https://github.com/pallets/werkzeug/blob/5a2bf35441006d832ab1ed5a31963cbc366c99ac/werkzeug/utils.py#L35
"""
import functools


class LazyProperty:
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


def lazy_property(fn):
    attr = '_lazy__' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)

    return _lazy_property


class Person:
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby
        self.call_count = 0

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        relatives = 'Many relatives.'
        return relatives

    @LazyProperty
    def parents(self):
        self.call_count += 1
        return 'Father and mother'


if __name__ == '__main__':
    john = Person('John', 'Coder')
    print(f'Name: {john.name}')
    print(f'Hobby: {john.hobby}', end='\n\n')

    print('Before we access `relatives`')
    print(sorted(john.__dict__.items()), end='\n\n')

    print("After we've accessed `relatives`")
    print(f'Relatives: {john.relatives}')
    print(sorted(john.__dict__.items()))
    print(f'Parents: {john.parents}', end='\n\n')

    print(john.__dict__.items())
    print(f'Parents: {john.parents}')
    print(f'Count: {john.call_count}')
