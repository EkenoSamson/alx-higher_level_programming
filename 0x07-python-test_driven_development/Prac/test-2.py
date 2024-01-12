#!/usr/bin/python3
# Using pytest

def test_sum_numbers_using_pytest():
    assert sum([700, 900]) == 1600, "Result should be 1600"

def test_sum_tuple_using_pytest():
    assert sum((700, 1900)) == 1600, "Result should be 1600"

test_sum_numbers_using_pytest()
test_sum_tuple_using_pytest()
