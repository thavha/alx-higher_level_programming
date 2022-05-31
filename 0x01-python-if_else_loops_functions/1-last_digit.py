#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(str(number)[-1])
cond = ""
if number < 0:
    last = -last
if last > 5:
    cond = "and is greater than 5"
elif last == 0:
    cond = "and is 0"
else:
    cond = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last} {cond}")
