# -*- coding: utf-8 -*-
"""
Created on Sat May 25 09:09:39 2019

@author: Michael
"""

"""
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, , or a downhill,  step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

For example, if Gary's path is , he first enters a valley  units deep. Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.
"""

"""
Function Description

Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.

countingValleys has the following parameter(s):

n: the number of steps Gary takes
s: a string describing his path
"""

"""
Input Format

The first line contains an integer , the number of steps in Gary's hike.
The second line contains a single string , of  characters that describe his path.
"""

"""
Output Format

Print a single integer that denotes the number of valleys Gary walked through during his hike.
"""

import math
import os
import random
import re
import sys

def countingValleys(n, s):

    # initialisation of the current level, where
    # =0 represents sea level
    # >0 represents highier level
    # <0 represents lower level
    current_level = 0

    # initialisation of the number of mountains
    num_mountains = 0

    # initialisation of the number of valleys
    num_valleys = 0

    for i in range(0,n - 1, 2):

        # if {UU}, current_level add 1
        if s[i] == 'U' and s[i + 1] == 'U':
            current_level += 1
            # if cross sea level, a valley found
            if current_level < 0 and (current_level + 1) >= 0:
                num_valleys += 1
            current_level += 1
        # if {UD}, current_level subtract 1
        elif s[i] == 'U' and s[i + 1] == 'D':
            current_level += 1
            # if cross sea level, a mountain found
            if current_level > 0 and (current_level - 1) <= 0:
                num_mountains += 1
            current_level -= 1
        # if {DD}, current level subtract 1
        elif s[i] == 'D' and s[i + 1] == 'D':
            current_level -= 1
            # if cross sea level, a mountain found
            if current_level > 0 and (current_level - 1) <= 0:
                num_mountains += 1
            current_level -= 1
        # if {DU}, current level add 1
        elif s[i] == 'D' and s[i + 1] == 'U':
            current_level -= 1
            # if cross sea level, a valley found
            if current_level < 0 and (current_level + 1) >= 0:
                num_valleys += 1
            current_level += 1
    print("Number of Mountains is {}, Number of Valleys is {}.".format(num_mountains,
          num_valleys))

    return num_valleys





























