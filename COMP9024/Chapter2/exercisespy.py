# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:29:53 2019

@author: Michael
"""

"""
R-2.1 Give three examples of life-critical software applications
"""
print("Life-critical software system is a system whose failure or malfunction may \
      result in one of the following outcomes.\
      Infrustructure; Medicine; and Nuclear engineering.")

"""
R-2.4 Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number of petals,
and its price. Your class must include a constructor method that initializes each variable
to an appropriate value, and your class should include methods for setting the value of
each type, and retrieving the value of each type.
"""
class Flower:
    """ to-be-selled Flower """

    def __init__(self, name, petals, price):
        """ Create a new Flower instance

        name: the name of the flower
        num_petals: the number of the petals
        price: the price of this flower instance
        """

        self._name = name
        self._petals = petals
        self._price = price

    def set_name(self, name):
        self._name = name

    def set_petals(self, petals):
        self._petals = petals

    def set_price(self, price):
        self._price = price

    def get_name(self):
        return self._name

    def get_petals(self):
        return self._petals

    def get_price(self):
        return self._price

