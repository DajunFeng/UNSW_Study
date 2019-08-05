# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:53:36 2019

@author: Michael
"""

import math
import os
import random
import re
import sys

def repeated_string(s, n):
    """ Return the number of of letter a's in the first n letters of the infinite
    string created by repeating s infinitely many times
    """

    result = 0

    unit_num = 0
    for letter in s:
        if letter == 'a':
            unit_num += 1

    unit_len = len(s)

    result = unit_num * (n // unit_len)

    modulo = 0
    if n % unit_len:
        modulo = n % unit_len

    if modulo == 1 and s[0] == 'a':
        result += 1
    else:
        if modulo > 1:
            for letter in s[:modulo]:
                if letter == 'a':
                    result += 1

    return result


