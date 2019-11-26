import ArrayStack

def is_matched(expression):
    """ Return True if all delimiters are properly match; False otherwise """

    lefty = '([{'
    righty = ')]}'
    stack = ArrayStack.ArrayStack()

    for c in expression:

        if c in lefty:
            stack.push(c)

        elif c in righty:
            if stack.is_empty():
                return False

            if righty.index(c) != lefty.index(stack.pop()):
                return False

    return stack.is_empty()
