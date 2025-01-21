#!/usr/bin/python3

def multiple_returns(sentence):

    result = (len(sentence), sentence[0]) \
        if sentence is not None else (len(sentence), None)

    return result
