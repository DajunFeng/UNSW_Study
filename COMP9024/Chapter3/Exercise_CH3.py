# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 16:02:25 2019

@author: Michael
"""

"""
R-3.1: Graph the functions 8n, 4nlogn, 2n^2, n^3, and 2^n using a logarithmic scale for
       the x- and y-axes; that is, if the function value f(n) is y, plot this as a point
       with x-coordinate at logn and y-coordinate at logy
"""
import matplotlib.pyplot as plt
import numpy as np

def graph_functions():
    """ Return the graphs """

    #print("8n graph in a logarithmic scale can be shown as following: ")
    _x1 = [10, 100000]
    _y1 = [8*i for i in _x1]

    x1 = [np.log2(i) for i in _x1]
    y1 = [np.log2(j) for j in _y1]
    plt.plot(x1, y1, label='f(n)=8n' )



    #print("4*n*log n graph in a logarithmic scale can be shown as following: ")
    _x2 = [10, 100000]
    _y2 = [4*n*np.log2(n) for n in _x2]

    x2 = [np.log2(n) for n in _x2]
    y2 = [np.log2(n) for n in _y2]
    plt.plot(x2, y2, label='f(n)=4*n*logn')

    #print("2n^2 graph in a logarithmic scale can be shown as following: ")
    _x3 = [10, 100000]
    _y3 = [2*n**2 for n in _x3]

    x3 = [np.log2(n) for n in _x3]
    y3 = [np.log2(n) for n in _y3]
    plt.plot(x3, y3, label='f(n)=2n^2')

    _x4 = [10, 100000]
    _y4 = [n**3 for n in _x4]

    x4 = [np.log2(n) for n in _x4]
    y4 = [np.log2(n) for n in _y4]
    plt.plot(x4, y4, label='f(n)=n^3')

    _x5 = [10, 1000]
    _y5 = [2**n for n in _x5]

    x5 = [np.log2(n) for n in _x5]
    y5 = [np.log2(float(n)) for n in _y5]
    plt.plot(x5, y5, label='f(n)=2^n')

    plt.legend()
    plt.figure()

"""
R-3.2: The number of operations executed by algorithms A and B is 8nlogn and 2n^2,
       respectively.
       Determine n0 such that A is better than B for n >= n0.
"""
def question_2_function():
    """ Return the n0 such that A is better than B for n >= n0 """

    not_found = True
    n0 = 1

    while(not_found):
        a = 8 * n0 * np.log2(n0)
        b = 2 * n0 ** 2

        if a == b:
            not_found = False
            return n0
        else:
            n0 += 1
            continue




