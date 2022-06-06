#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return tuple((None,sentence[0]))
    else:
        return tuple((length,sentence[0]))

