'''importing union'''
from typing import Union

# Define a type alias for numbers (both int and float)

Number = Union[int, float]

# typehinting a & b as Numbers (int or float)
# each function should return a Number (int or float)
def addition(a: Number,b: Number) -> Number:
    '''addition'''
    return a + b

def subtraction(a: Number,b: Number) -> Number:
    '''function'''
    return a - b

def multiplication(a: Number,b: Number) -> Number:
    '''multiplication'''
    return a * b

def division(a: Number,b: Number) -> Number:
    '''division'''
    return a / b
