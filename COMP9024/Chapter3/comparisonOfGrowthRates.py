# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:49:11 2019

@author: Michael
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(500, 1000, 100)

plt.title('Comparison of Growth Rates')

c = 1
#plt.plot(x, c, label='Constant')
plt.plot(x, np.log2(x), label='Logarithm')
plt.plot(x, x, label='Linear')
plt.plot(x, x*np.log2(x), label='n-log-n')
plt.plot(x, x*x, label='Quadratic')
plt.plot(x, x**3, label='Cubic')
plt.plot(x, 2**x, label='Exponential')

plt.xlabel('n')
plt.ylabel('f(n)')

plt.legend()

plt.show()
