#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    str_tuple = (sentence,)
    return (len(str_tuple[0]), str_tuple[0][0])
