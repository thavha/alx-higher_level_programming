#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    else:
        length = len(sys.argv) 
        print("{} arguments:".format(length-1))
        for i in range(2,length+1):
            print("{}: {}".format(i-1,sys.argv[i-1]))