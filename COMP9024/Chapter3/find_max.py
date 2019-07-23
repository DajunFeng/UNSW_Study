# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 09:30:21 2019

@author: Michael
"""

def find_max(num_list):
    """ Return the largest number in the list """

    largest_num = num_list[0]

    for number in num_list:

        if largest_num < number:
            largest_num = number

    return largest_num