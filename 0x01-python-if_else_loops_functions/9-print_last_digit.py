#!/usr/bin/python3
def print_last_digit(number):
    last = int(str(number)[-1])
    if number < 0:
        last = -last
    return last
