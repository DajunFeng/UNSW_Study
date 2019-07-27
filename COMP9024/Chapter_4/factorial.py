# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 10:11:48 2019

@author: Michael
"""

def factorial(n):
    """ Return the fatorial result of n """

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

