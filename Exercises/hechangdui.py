# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:59:56 2019

@author: Michael
"""

global maximum

def _lis(arr, n ):

    # to allow the access of global variable
    global maximum

    # Base Case
    if n == 1 :
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1

    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
       IF arr[n-1] is maller than arr[n-1], and max ending with
       arr[n-1] needs to be updated, then update it"""
    for i in xrange(1, n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1

    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum, maxEndingHere)

    return maxEndingHere
def lis(arr):

    # to allow the access of global variable
    global maximum

    # lenght of arr
    n = len(arr)

    # maximum variable holds the result
    maximum = 1

    # The function _lis() stores its result in maximum
    _lis(arr, n)

    return maximum

