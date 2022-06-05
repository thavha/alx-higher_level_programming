#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum_ = 0
    for i in sys.argv[1:]:
        sum_ += int(i)
    print(sum_)
