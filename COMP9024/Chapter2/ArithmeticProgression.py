# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:29:03 2019

@author: Michael
"""
import Progression

class ArithmeticProgression(Progression):
    """ Iterator producing an arithmetic progression """

    def __init__(self, increment = 1, start = 0):
        """ Create a new arithmetic progression

        increment   the fixed constant to add to each term (default 1)
        start       the first term of the progression
        """

        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """ Update current value by adding the fixed increment """

        self._current += self._increment

