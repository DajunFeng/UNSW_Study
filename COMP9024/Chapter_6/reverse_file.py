import ArrayStack

def reverse_file(filename):
    """ Overwrite given file with its contents line-by-line reversed. """

    stack = ArrayStack.ArrayStack()

    with open(filename, 'r') as file:
        for line in file:
            stack.push(line.rstrip('\n'))

    while not stack.is_empty():
        with open(filename, 'w') as file:
            file.write(stack.pop() + '\n')
