# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:59:51 2019

@author: Michael
"""
class Empty(Exception):
    pass

class ArrayQueue:
    """ FIFO queue implementation using a Python list as underlying storage """

    DEFAULT_CAPACITY = 10

    def __init__(self):
        """ Create an emtpy queue """

        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """ Return the number of elements in the queue """

        return self._size

    def is_empty(self):
        """ Return True if the queue is empty """

        return self._size == 0

    def first(self):
        """ Return (but not remove) the element at the front of the queue
        Raise Empty exception if the queue is empty
        """

        if self.is_empty():
            raise Empty("Queue is empty!")

        return self._data[self._front]

    def dequeue(self):
        """ Return (and remove) the element at the front of the queue
        Raise Empty exception if the queue is empty
        """

        if self.is_empty():
            raise Empty("Queue is empty!")

        answer = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data)//2)
        self._front = (self._front + 1) % len(self._data)

        return answer

    def _resize(self, cap):
        """ Resize to a new list of capacity >= len(self). """

        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


    def enqueue(self, element):
        """ Add an element to the back of the queue. """

        if self._size == len(self._data):
            self._resize(2*len(self._data))

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = element
        self._size += 1












