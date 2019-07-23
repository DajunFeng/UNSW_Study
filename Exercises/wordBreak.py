# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:39:15 2019

@author: Michael
"""

def wordBreak(s, sdict):
    dp = [False for i in range(len(s)+1)]
    dp[0] = True
    for i in range(1, len(s)+1):
        for k in range(i):
            if dp[k] and s[k:i] in sdict:
                dp[i] = True
    return dp[len(s)]
