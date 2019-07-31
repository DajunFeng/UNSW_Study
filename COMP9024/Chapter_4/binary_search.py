# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:12:57 2019

@author: Michael
"""

"""
Binary Search: efficiently locate a target value within a sorted sequence of n elements

"""

def binary_search(a, target, low, high):
    """ Return True if target is found in indicated portion of data list """

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == a[mid]:
            return True
        elif target < a[mid]:
            return binary_search(a, target, low, mid-1)
        elif target > a[mid]:
            return binary_search(a, target, mid+1, high)