# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:38:20 2019

@author: Michael
"""

class Vector:
    """ Represent a vector in a multidimensional space """

    def __init__(self, d):
        """ Create or initialize a d-dimensional vector of zeros """

        self._coordinates = [0] * d

    def __len__(self):
        """ Return the dimension of the vector """
        return len(self._coordinates)

    def __getitem__(self, j):
        """ Return the jth dimension of the vector """
        return self._coordinates[j]

    def __setitem__(self, j, value):
        """ Set jth coordinate of the vector to be the given value """
        self._coordinates[j] = value

    def __add__(self, another_vector):
        """ Return the sum of the 2 vectors """

        if len(self) != len(another_vector):
            raise ValueError('Dimensions must agree! ')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + another_vector[j]
        return result

    def __eq__(self, other):
        """ Return True if vector has the same coordinates as other """
        return self._coordinates == other._coordinates

    def __ne__(self, other):
        """ Return True if vector differs from other """
        return not self == other

    def __str__(self):
        """ Produce string representation of vector """

        return '<' + str(self._coordinates)[1: -1] + '>'
