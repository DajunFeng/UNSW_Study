# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 09:02:28 2019

@author: Michael
"""
"""
Complete the 'diagonalDifference' function below.

The function is expected to return an INTEGER.
The function accepts 2D_INTEGER_ARRAY arr as parameter.
"""

def diagonalDifference(arr):
    """ Return the difference between primary diagonal and secondary diagonal """

    primary = []
    for i in range(len(arr)):
        for k in range(len(arr)):
            if i == k:
                primary.append(arr[i][k])

    secondary = []
    standard = len(arr) - 1

    for i in range(len(arr)):
        for k in range(len(arr)):
            if i + k == standard:
                secondary.append(arr[i][k])

    return abs(sum(primary) - sum(secondary))

