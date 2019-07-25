# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:43:31 2019

@author: Michael
"""

def unique_2(s):
    """ Return True if all elements in list S are distinct  """

    temp = sorted(s)

    for i in range(len(temp)-1):
        if temp[i] == temp[i+1]:
            return False

    return True


