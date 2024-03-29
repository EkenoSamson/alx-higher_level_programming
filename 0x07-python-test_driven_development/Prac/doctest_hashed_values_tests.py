#!/usr/bin/python3
# doctest_hashed_values_tests.py


import collections

def group_by_length(words):
    """ Returns a dictionary grouping words into sets length.

    >>> grouped = group_by_length(['Python', 'module', 'of', 'the', 'week'])
    >>> grouped = { 2:set(['of']),
    ...             3:set(['the']),
    ...             4:set(['week']),
    ...             6:set(['python', 'module']),
    ...             }
    True
    """

    d = collections.defaultdict(set)
    for word in words:
        d[len(word)].add(word)
    return d
