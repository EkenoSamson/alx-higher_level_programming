#!/usr/bin/python3
"""class Square"""


class Square:
    """
    Classs definition

    Args: size - size of the square(optional).
          value - sets the value of size.
    """

    def __init__(self, size=0):
        """class initialiser"""
        self.size = size

    @property
    def size(self):
        """size accessor"""
        return self.__size

    @size.setter
    def size(self, value):
        """size mutator"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """print square using  #"""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
