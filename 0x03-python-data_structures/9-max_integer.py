#!/usr/bin/python3
from re import M


def max_integer(my_list=[]):
    m = 0
    for i in my_list:
        if i > m:
            m = i
    return m

