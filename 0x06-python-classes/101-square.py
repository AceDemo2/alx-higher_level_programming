#!/usr/bin/python3
"""
class Square
"""


class Square:
    """
    define square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize square
        Args: size (int): size of the square and position
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 \
                or type(value[0]) is not int or type(value[1]) is not int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                for j in range(self.__size):
                    print("#", end='')
                print()

    def __str__(self):
        i = ""
        if self.__size == 0:
            return ""
        else:
            for k in range(self.__position[1]):
                i += "\n"
            for le in range(self.__size):
                i += " " * self.__position[0]
                for m in range(self.__size):
                    i += "#"
                i += "\n" if le < self.__size - 1 else ""
        return i
