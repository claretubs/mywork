# Program takes a number and returns a lsit containing a Fibbonacci sequence of that many numbers
# Testing Errors
# Author: Clare Tubridy
# Date: 11/04/2023

import logging
# logging.basicConfig(level=logging.DEBUG)

def fibbonacci(number):
    if number == 0:
        return []
    elif number < 0:
        raise ValueError('Number must be > 0')
    a = 0
    b = 1
    fibbonacci_sequence = [0]
    # we have one in the list already so number -1 times
    # this is not the most efficent code
    # could have used yield
    for i in range(1,number):
        fibbonacci_sequence.append(b)
        # this is funky code make a = b and b = a + b
        a , b = b, a + b
    logging.debug("%d: %s", number, fibbonacci_sequence)
try:
    fibbonacci(-1)
except ValueError:
    # we want this exception to be thrown
    # so this is an example where we want to do nothing
    pass
else:
    # if the execption was not thrown we should throw
    # Assertion error
    assert False, 'Fibonacci missing ValueError'
    # or 
    # raise AssertionError('Fibonacci no ValueError')

# Test Cases
'''
return7 = [0,1,1,2,3,5,8]
return11 = [0,1,1,2,3,5,8,13,21,34,55]
assert fibbonacci(7) == return7, 'Incorrect return for 7'
assert fibbonacci(11) == return11, 'Incorect return for 11'
assert fibbonacci(0) == [], 'Incorrect return for 0'
assert fibbonacci(1) == [1], 'Incorrect return for 1'
'''
if __name__ == "__main__":
    # Tests will go here
    print("All Good")