# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:37:57 2019

@author: Michael
"""

def unique_1(s):
    """ Return True if all elements in list s are distinct """

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:

                return False
    return True