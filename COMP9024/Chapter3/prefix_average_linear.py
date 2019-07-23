# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:09:32 2019

@author: Michael
"""

def prefix_average_linear(s):
    """ Return the prefix average number array of array n """

    n = len(s)
    a = [0] * n

    total = 0
    for i in range(n):
        total += s[i]
        a[i] = total / (i + 1)

    return a