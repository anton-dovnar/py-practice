"""
The Borg pattern (also known as the Monostate pattern) is a way to
implement singleton behavior, but instead of having only one instance
of a class, there are multiple instances that share the same state. In
other words, the focus is on sharing state instead of sharing instance
identity.

Usually, each instance will have its own dictionary, but the Borg pattern
modifies this so that all instances have the same dictionary.
In this example, the _shared_state attribute will be the dictionary
shared between all instances, and this is ensured by assigining
_shared_state to the __dict__ variable when initializing a new
instance (i.e., in the __init__ method). Other attributes are usually
added to the instance's attribute dictionary, but, since the attribute
dictionary itself is shared (which is _shared_state), all other
attributes will also be shared.

A singleton with shared-state among instances.
"""


class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class YourBorg(Borg):

    def __init__(self, state=None):
        super().__init__()
        if state:
            self.state = state
        else:
            # initiate the first instance with default state
            if not hasattr(self, 'state'):
                self.state = 'Init'

    def __str__(self):
        return self.state


if __name__ == '__main__':
    rm1 = YourBorg()
    rm2 = YourBorg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print(f'rm1: {rm1}')
    print(f'rm2: {rm2}')

    # When the `state` attribute is modified from instance `rm2`,
    # the value of `state` in instance `rm1` also changes
    rm2.state = 'Zombie'
    print(f'rm1: {rm1}')
    print(f'rm2: {rm2}')

    # Even though `rm1` and `rm2` share attributes, the instances are not the same
    print(rm1 is rm2)

    # New instances also get the same shared state
    rm3 = YourBorg()
    print(f'rm1: {rm1}')
    print(f'rm2: {rm2}')
    print(f'rm3: {rm3}')

    # A new instance can explicitly change the state during creation
    rm4 = YourBorg('Running')
    print(f'rm4: {rm4}')

    # Existing instances reflect that change as well
    print(f'rm3: {rm3}')
