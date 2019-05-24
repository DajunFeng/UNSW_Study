# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:07:37 2018

@author: Michael
"""

"""
Chapter 1: Python Primer
"""

"""
Question 1
Write a short python function, is_multiple(n, m), that takes two integer values and
returns True if n is a multiple of m, that is, n = m * i for some integer i, and
False otherwise.
"""

def is_multiple(n, m):

    if n % m == 0:
        return True
    else:
        return False

"""
Question 2
Write a short python function, is_even(k), that takes an integer value and returns
True if k is even, and False otherwise.
However, your function cannot use the multiplication, modulo, or division operators.
"""

def is_even(k):

    if k & 1:
        return True
    else:
        return False

"""
Question 3
Write a short python function, minmax(data), that takes a sequence of one or more
numbers, and returns the smallest and largest numbers, in the form of a tuple of
length two.
Do not use the built-in functions min or max in implementing your solution.
"""

def minmax(data):

    minimum_number = data[0]
    maximum_number = data[0]

    for number in data:

        print("iterating at {}".format(number))

        print("getting minimum number")
        if minimum_number >= number:
            minimum_number = number

        print("getting maximum number")
        if maximum_number <= number:
            maximum_number = number


    return minimum_number, maximum_number

"""
Question 4
Write a short python function that takes a positive integer n and returns the sum of
the squares of all the positive integers smaller than n
"""

def square_sum(n):

    l = [i**2 for i in range(n)]
    print("The generated list is {}".format(l))
    result = sum(l)

    return result

"""
Question 5
Give a single command that computes the sum from question 4, relying on Python's
comprehension syntax and the built-in sum function
"""
print(sum([i**2 for i in range(eval(input("Enter a positive integer: ")))]))

"""
Question 6
Write a short Python function that takes a positive integer n and returns the sum of
the squares of all the odd positive integers smaller than n
"""
def odd_square_sum(n):

    l = [i**2 for i in range(n) if i&1]
    print("The generated list is {}".format(l))
    result = sum(l)

    return result

"""
Question 7
Give a single command that computes the sum from question 6 relying on Python's
comprehension syntax and the built-in sum function
"""
print(sum([i**2 for i in range(eval(input("Enter a positive integer: "))) if i&1]))

"""
Question 8
Python allows negative integers to be used as indices into a squence, such as a string
If string s has length n, and expression s[k] is used for index -n<k<0
What is the equivalent index j>=0 such that s[j] references the same element.
"""
#j = n + k

"""
Question 9
What parameters should be sent to the range constructor, to produce a range with values
50, 60, 70, 80
"""
values = [i for i in range(50, 90, 10)]

"""
Question 10
What parameters should be sent to the range constructor, to produce a range with
values 8, 6, 4, 2, 0, -2, -4, -6, -8?
"""

values_10 = [i for i in range(-8, 9, 2)]
print(values_10)

"""
Question 11
Demonstrate how to use Python's list comprehension syntax to produce the list
[1, 2, 4, 8, 16, 32, 64, 128, 256]
"""

list_11 = [2**i for i in range(9)]
print(list_11)

"""
Question 12
Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes
a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""
def my_choice(data):

    import random

    index = random.randrange(len(data))

    return data[index]

"""
Question 13
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""
def my_reverse(data):

    reversed_list = [0] * len(data)

    for i in range(len(data)):

        reversed_list[i] = data[-1-1*i]

    return reversed_list

"""
Question 14
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""

def odd_product(data):

    num_odd_product = 0
    for i in range(len(data) - 1):
        for j in range(i+1, len(data)):
            product = data[i] * data[j]
            if product & 1:
                print("{} and {} have the product {}".format(data[i], data[j], product))
                num_odd_product += 1

    print(num_odd_product)
    if num_odd_product == 1:
        return True
    else:
        return False

"""
Question 15
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""

def is_distinct_elements(data):

    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return False
            else:
                continue
    return True


"""
Question 18
Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
"""

list_18 = [i*(i+1) for i in range(10)]
print(list_18)

"""
Question 19
Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
"""

list_19 = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(list_19)

"""
Question 20
Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
"""

def my_shuffle(data):

    import random

    index_list = []

    shuffled_list = [0] * len(data)

    for number in data:
        current_index = random.randint(0, len(data) - 1)
        while current_index in index_list:
            current_index = random.randint(0, len(data) - 1)
        index_list.append(current_index)
        shuffled_list[current_index] = number

    print(index_list)
    return shuffled_list

"""
Question 21
Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""

























