
class Empty(Exception):

    pass

class ArrayStack:
    """ LIFO (Last In First Out) Stack implementation using a Python list as underlying storage """

    def __init__(self):
        """ Create an empty stack """

        self._data = []

    def __len__(self):
        """ Return the number of elements in the stack """

        return len(self._data)

    def is_empty(self):
        """ Return True if the stack is empty """

        return len(self._data) == 0

    def push(self, element):
        """ Add element to the top of the stack """

        self._data.append(element)

    def top(self):
        """ Return but not remove the element at the top of the stack """

        if self.is_empty():
            raise Empty("Stack is empty! there can be no top element.")

        else:
            return self._data[-1]

    def pop(self):
        """ Remove and Return the element at the top of the stack """

        if self.is_empty():
            raise Empty("Stack is empty! there can be no top element.")
        else:
            return self._data.pop()
