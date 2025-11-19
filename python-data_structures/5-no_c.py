#!/usr/bin/python3
def no_c(text):
    a = ''
    for i in text:
        if i not in "cC":
            a = a + i
    return a
