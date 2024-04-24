#!/usr/bin/python3
"""
class Square
"""


class Square:
    """
    define square
    """
    def __init__(self, size=0):
        """initialize square
        Args: size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def __e__(self, i):
        return self.size == i.size

    def __ne__(self, i):
        return self.size != i.size

    def __lt__(self, i):
        return self.size < i.size

    def __le__(self, i):
        return self.size <= i.size

    def __gt__(self, i):
        return self.size > i.size

    def __ge__(self, i):
        return self.size >= i.size
