#!/usr/bin/python3
import sys


def main():

    a = sys.argv[1:]
    length = len(a)
    i = 0
    while i < len(a):
        try:
            a[i] = int(a[i])
            i + =1
        except Exception:
            a.pop(i)
        print(sum(a))


if __name__ == "__main__":
    main()
