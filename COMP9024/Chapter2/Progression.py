# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:21:37 2019

@author: Michael
"""

class Progression:
    """ Iterator producing a generic progression

    Default iterator produces the whole numbers 0, 1, 2, ....

    """

    def __init__(self, start = 0):
        """ Initialize current to the first value 0 """

        self._current = start

    def _advance(self):
        """ Update self.current to a new value
        This should be overriden by a subclass to customize progression

        By convention, if current is set to None, get the end of a finite progression
        """

        self._current += 1

    def __next__(self):
        """ Return the next value, or raise StopIteration Error """
        if self._current is None:
            raise StopIteration()
        else:
            self._advance()
            answer = self._current

            return answer

    def __iter__(self):
        """ By convention, an iterator must return itself as an iterator """
        return self

    def print_progression(self, n):
        """ Print next n values of the progression """
        print(' '.join(str(next(self)) for j in range(n)))