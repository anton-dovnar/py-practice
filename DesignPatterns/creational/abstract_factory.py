import random
from dataclasses import dataclass


@dataclass
class Pet:
    name: str

    def speak(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


@dataclass
class Dog(Pet):
    def speak(self) -> None:
        print('woof\n')

    def __str__(self) -> str:
        return f'Dog<{self.name}>'


@dataclass
class Cat(Pet):
    def speak(self) -> None:
        print('meow\n')

    def __str__(self) -> str:
        return f'Cat<{self.name}>'


@dataclass
class PetShop:
    pet_factory: Pet

    def buy_pet(self, name: str) -> Pet:
        pet = self.pet_factory(name)
        print(f'Here is your lovely {pet}')
        return pet


def random_animal(name: str) -> Pet:
    return random.choice([Dog, Cat])(name)


if __name__ == '__main__':
    cat_shop = PetShop(Cat)
    pet = cat_shop.buy_pet('Lucy')
    pet.speak()

    shop = PetShop(random_animal)
    for name in ['Max', 'Jack', 'Buddy']:
        pet = shop.buy_pet(name)
        pet.speak()
