"""
Complete the staircase function.
It should print a staircase as described
Parameters:
    N: an integer, denoting the size of the staircase

"""
import math
import os
import random
import re
import sys

def staircase(n):

    for level in range(1, n+1):
        blank = n - level
        line = blank * ' ' + level * '#'
        print(line)
