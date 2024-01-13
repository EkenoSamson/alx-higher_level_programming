#!/usr/bin/python3
# doctest_unpredictable.py


class MyClass:
    pass

def unpredictable(obj):
    """ Returns a newlist containing obj.

    >>> unpredictable(MyClass())
    [<doctest_unpredictable.MyClass object at 0x10055a2do>]
    """
    return [obj]
