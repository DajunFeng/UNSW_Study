# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:51:31 2019

@author: Michael
"""

def prefix_average(s):
    """ Return the prefix average number array of array s """

    # initialisation of the array a
    a = [0] * len(s)

    # iteration
    for i in range(len(s)):
        a[i] = sum(s[0: (i+1)]) / (i+1)

    return a