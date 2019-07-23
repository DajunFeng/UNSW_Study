# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:32:18 2019

@author: Michael
"""

def disjoint_2(a, b, c):
    """ Return True if there is no element common to all three lists a, b and c """

    for i in a:
        for j in b:
            if i == j:
                for k in c:
                    if i == k:
                        return False
    return True