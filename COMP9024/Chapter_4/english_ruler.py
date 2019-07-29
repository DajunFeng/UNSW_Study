# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:09:50 2019

@author: Michael
"""

"""
specification:
    The English ruler pattern can be a shape that has a self-recursive structure at
    various levels of magnification.
    the major tick length is 5 '----- 1'; '----- 2'; etc.
    the 1/2 inch tick length is 4
    the 1/4 inch tick length is 3
    the 1/8 inch tick length is 2
    the 1/16 inch tick length is 1
"""

def draw_ruler(num_inches, major_length):
    """ Draw English ruler with given number of inches, major length of tick """

    draw_line(major_length, '0')

    for i in range(1, num_inches+1):
        draw_interval(major_length-1)
        draw_line(major_length, str(i))

def draw_line(tick_length, tick_label=''):
    """ Draw one line with given tick_length (with optional label) """

    line = '-' * tick_length
    if tick_label:
        line += tick_label
    print(line)

def draw_interval(center_length):
    """ Draw the interval between inch labels """

    if center_length > 0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)








