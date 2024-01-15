#!/usr/bin/python3
"""

Module contains class Phone

"""


class Phone:
    """
    This is a blueprint for phone

    Args:
        screen_size - display ratio
        no_of_buttons - number of buttons

    Raise
        TypeError - expecting integer values.
        ValueError - less than five number of buttons.
    """
    def __init__(self, screen_size, no_of_buttons):
        """ The object constructor"""
        self.screen_size = screen_size
        self.no_of_buttons = no_of_buttons

    @property
    def no_of_buttons(self):
        """the number of buttons retriever"""
        return self.__no_of_buttons

    @no_of_buttons.setter
    def no_of_buttons(self, value):
        """mutator for number of buttons"""
        if type(value) is not int: # if not isinstance(value, int)
            raise TypeError("no_of_button must be an integer")
        if value >= 5:
            raise ValueError("no_of_buttons must be less than five")
        self.__no_of_buttons = value

    def weight(self):
        """return the phone mass"""
        return (self.screen_size * self.__no_of_buttons)
