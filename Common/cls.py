"""
@classmethod is bound to a class. @staticmethod is similar to a
python function but define in a class.
"""
from abc import ABCMeta, abstractmethod


class Base:
    """ abc is used to define methods but not implement """
    __metaclass__ = ABCMeta

    @abstractmethod
    def absmethod(self):
        """ Abstract method """


class Example(Base):

    def absmethod(self):
        print('abstract')


class Base2:
    """ Another common way """

    def absmethod(self):
        raise NotImplementedError


class Example2(Base2):

    def absmethod(self):
        print('abstract')


if __name__ == '__main__':
    ex = Example()
    ex.absmethod()

    ex2 = Example2()
    ex2.absmethod()
