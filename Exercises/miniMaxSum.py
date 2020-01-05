#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Michael
#
# Created:     05/01/2020
# Copyright:   (c) Michael 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def miniMaxSum(arr):

    sorted_arr = sorted(arr)

    min_sum = sum(sorted_arr[:4])
    max_sum = sum(sorted_arr[1:])

    print(min_sum, max_sum)

