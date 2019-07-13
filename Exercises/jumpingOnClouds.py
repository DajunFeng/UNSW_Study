# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 08:18:39 2019

@author: Michael
"""

"""
Problem:
    Emma is playing a new mobile game that starts with consecutively numbered clouds.
    Some of the clouds are thunderheads and others are cumulus.
    She can jump on any cumulus cloud having a number that is equal to the number of
    the current cloud plus 1 or 2.
    She must avoid the thunderheads.
    Determine the minimum number of jumps it will take Emma to jump from her starting
    position to the last cloud. It is always possible to win the game.

    For each game, Emma will get an array of clouds numbered 0 if they are safe while
    1 if they must be avoided.

Function description:
    jumpOnClouds() should return the minimum number of jumps required, as an integer
    parameters: an array of binary integers

Input format:
    The first line contains an integer n, the total number of clouds
    The second line contains n space-separated binary integers describing clouds c[i]
    where 0 <= i < n

Constraints:
    2 <= n <= 100
    c[i] in {0, 1}
    c[0] = c[-1] = 0

output format:
    Print the minimum number of jumps needed to win the game
"""
import math
import os
import random
import re
import sys

def jumping_on_clouds(clouds_list):
    """ Return the minimum number of the jumps """

    jumps = 0
    iter_list = list(clouds_list)

    while len(iter_list):
        print("---------Current list {}----------".format(iter_list))

        if 1 in iter_list:
            print("still need dividing from the first 1")
            one_index = iter_list.index(1)
            pri_part = iter_list[0: one_index]
            iter_list = iter_list[one_index+1:]

            if len(pri_part) <= 1:
                jumps += 1
                continue
            else:
                if len(pri_part) % 2 == 0:
                    jumps += len(pri_part) / 2
                else:
                    jumps += (len(pri_part) - 1) / 2

            jumps += 1

        else:
            if len(iter_list) == 1:
                break
            else:
                if len(iter_list) % 2 == 0:
                    jumps += len(iter_list) / 2
                else:
                    jumps += (len(iter_list) - 1) / 2
                break

    return int(jumps)





















