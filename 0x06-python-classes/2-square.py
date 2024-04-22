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
        Args:  size (int): size of the square 
        """
        if type(size) not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueEror('size must be >= 0')
        else:
            self.__size = size
