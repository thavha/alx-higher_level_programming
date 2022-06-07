#!/usr/bin/python3
def add_tuple(tuple_a=(0, 0), tuple_b=(0, 0)):
    if len(tuple_a) == 1:
        tuple_a = tuple((tuple_a[0], 0))
    if len(tuple_b) == 1:
        tuple_b = tuple((tuple_b[0], 0))
    if len(tuple_a) == 0:
        tuple_a = tuple((0, 0))
    if len(tuple_b) == 0:
        tuple_b = tuple((0, 0))
    return tuple((tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]))
