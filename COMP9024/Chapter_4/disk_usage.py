# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:47:33 2019

@author: Michael
"""

import os

def disk_usage(path):
    """ Return the number of bytes used by a file/folder and any descendents """

    total = os.path.getsize(path)
    if os.path.isdir(path):
        for file_name in os.listdir(path):
            child_path = os.path.join(path, file_name)
            total += disk_usage(child_path)

    return total