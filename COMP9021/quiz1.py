# Generates a list L of random nonnegative integers at most equal to some value
# input by the user, and of length also input by the user, and outputs a list
# consisting of the longest streak of consecutive occurrences of the same value in L,
# possibly looping around (as if the list was a ring). In the case multiple value
# have the longest streak of consecutive occurrences in L, then the smallest value is chosen.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randint


try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
print('\nThe generated list is:')
print('  ', L)

r = list(set(L))
d = {k:[] for k in r}

for i in range(len(L)):
    d[L[i]].append(i)

results = []

for key in d:
    sub_result = []
    for i in range(0, len(d[key]) - 1):
        if d[key][i]+1 == d[key][i+1]:
            sub_result.append(key)
        if 0 in d[key] and len(L)-1 in d[key]:
            sub_result.append(key)
    if not len(sub_result):
        sub_result.append(key)
    results.append(sub_result)
R = results[0]

for sub_result in results:
    if len(R) < len(sub_result):
        R = sub_result
    elif len(R) == len(sub_result) and R[0] > sub_result[0]:
        R = sub_result









print('\nThe longest streak of the same value is:')
print('  ', R)
