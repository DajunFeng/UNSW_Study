# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 09:29:54 2019

@author: Michael
"""

def plusMinus(arr):
    """ Print the decimal value of each fraction (the ratio of positive, negative
    and zero items in the array arr.)
    """

    length = len(arr)

    pos = 0
    neg = 0
    zero = 0

    for e in arr:
        if e > 0:
            pos += 1
        elif e < 0:
            neg += 1
        else:
            zero += 1

    print(round(pos/length, 6))
    print(round(neg/length, 6))
    print(round(zero/length, 6))