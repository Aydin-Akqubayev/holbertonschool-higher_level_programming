#!/usr/bin/python3
'''This code generates Pascal's triangle'''


def pascal_triangle(num):

    '''Generates Pascal's triangle for a given number of rows.'''

    res = []

    if num == 0:
        return res

    res.append([1])

    for i in range(1, num):
        row = [1]
        for j in range(1, len(res[i-1])):
            row.append(res[i-1][j-1] + res[i-1][j])
        row.append(1)
        res.append(row)

    return res
