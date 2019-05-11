# definition of a generator
def factor(n):
    
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k
"""
This function is an example of defining a python Generator
1. data type of generator: <Class 'generator'>
2. generator can be iterated to obtain all the elements in it
"""
