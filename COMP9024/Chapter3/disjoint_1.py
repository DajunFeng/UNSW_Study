# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:28:00 2019

@author: Michael
"""

def disjoint_1(a, b, c):
    """ Return True if there is no element common to all three lists a, b and c """

    for i in a:
        for j in b:
            for k in c:
                if i == j == k:
                    return False
    return True