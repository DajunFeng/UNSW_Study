# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:09:48 2019

@author: Michael
"""

"""
Question C-4.9:
Write a short recursive Python function that finds the minimum and maximum values in
a sequence without using any loops
"""
def min_max(sequence, index=0):

    if index == len(sequence) - 1:
        return sequence[index], sequence[index]
    else:
        min_value, max_value = min_max(sequence, index+1)
        return min(sequence[index], min_value), max(sequence[index], max_value)

"""
Question C-4.10:
Write a Python function to compute the integer part of the base-two logarithm of n
using only addition and integer division
"""
def int_logarithm(n):

    if n < 2:
        return 0
    else:
        return 1 + int_logarithm(n//2)

"""
Question C-4.11
Describe an efficient recursive function for solving the element uniqueness problem,
which runs in time that is at most O(n^2) in the worst case without using sorting.
"""
def uniqueness(array, index=0):

    if index == len(array) - 1:
        return True
    else:
        unique = True
        for i in range(index+1, len(array)):
            if array[index] == array[i]:
                unique = False
        return unique and uniqueness(array, index+1)

"""
Question C-4.12
Give a recursive algorithm to compute the product of two positive integers, m and n,
using only addition and substraction.
"""
def product(m, n):
    if m == 0 or n == 0:
        return 0
    else:
        return m + product(m, n-1)

"""
Question C-4.13
In section 4.2, we prove by induction that the number of lines printed by a call to
draw_interval(c) is 2^^c - 1. Another interesting question is how many dashes are printed
during that process. Prove by induction that the number of dashes printed by draw_interval(c)
is 2^^c - c - 2.
"""

"""
Question: C-4.15:
Write a recursive function that will output all the subsets of a set of n elements
"""

def subsets(s, n):
    """ Outputs all subsets of s """
    if n == 0:
        return [[]]
    else:
        return [[s[n-1]] + i for i in subsets(s, n-1)] + subsets(s, n-1)









