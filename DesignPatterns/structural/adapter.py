"""
Adapt one interface to another using a white-list.

The Adapter pattern provides a different interface for a class. We can
think about it as a cable adapter that allows you to charge a phone
somewhere that has outlets in a different shape. Following this idea,
the Adapter pattern is useful to integrate classes that couldn't be
integrated due to their incompatible interfaces.

The example has classes that represent entities (Dog, Cat, Human, Car)
that make different noises. The Adapter class provides a different
interface to the original methods that make such noises. So the
original interfaces (e.g., bark and meow) are available under a
different name: make_noise.
"""


class Dog:
    def __init__(self):
        self.name = 'Dog'

    def bark(self) -> str:
        return 'woof!'


class Cat:
    def __init__(self):
        self.name = 'Cat'

    def meow(self) -> str:
        return 'meow!'


class Human:
    def __init__(self):
        self.name = 'Human'

    def speak(self) -> str:
        return "'hello'"


class Car:
    def __init__(self):
        self.name = 'Car'

    def make_noise(self, octane_level: int) -> str:
        return f"vroom{'!' * octane_level}"


class Adapter:
    """Adapts an object by replacing methods.
    Usage
    ------
    dog = Dog()
    dog = Adapter(dog, make_noise=dog.bark)
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict."""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object."""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict."""
        return self.obj.__dict__


if __name__ == '__main__':
    objects = []
    dog = Dog()
    print(f'Dog: {dog.__dict__}\n')

    objects.append(Adapter(dog, make_noise=dog.bark))
    print(f'Adapter: {objects[0].original_dict()}\n')

    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))

    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))

    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    for obj in objects:
        print(f'A {obj.name} goes {obj.make_noise()}')
