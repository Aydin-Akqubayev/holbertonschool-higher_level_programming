#!/usr/bin/python3
import sys


def main():
    list_command = sys.argv
    length = len(list_command)
    if length - 1 > 1:
        print("{} arguments:".format(length - 1))
    elif length - 1 == 0:
        print("{} arguments.".format(length - 1))
    else:
        print("{} argument:".format(length - 1))
    for i in range(1, length):
        print("{}: {}".format(i, list_command[i]))


if __name__ == "__main__":
    main()
