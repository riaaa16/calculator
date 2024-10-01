'''importing abstract methods, unions, operations and number type alias'''
from abc import ABC, abstractmethod
from typing import Union
from app.operations import addition, subtraction, multiplication, division, Number

class Calculation(ABC):
    '''abstract calculation class'''
    # constructor initializing a & b
    # typehinting a & b as Numbers
    # -> None is telling Python that no value is being returned
    def __init__(self, a: Number, b: Number) -> None:
        # if the instances of a or b aren't ints or floats, raise an error
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both a and b must be numbers (int or float)")
        # self are class instances
        self.a = a
        self.b = b

    @classmethod
    # cls is like self for instance, and is used to access class variables
    def create(cls, a: Number, b: Number) -> 'Calculation':
        '''factory to create Calculation instances / copies'''
        return cls(a, b)
    # Every subclass provides its own version of this method.
    @abstractmethod
    def compute(self) -> Number:
        '''abstract method defining generic structure'''
        # No implementation here, subclasses will provide it.

# It inherits from the Calculation class and must implement the abstract method 'compute'.
class Addition(Calculation):
    '''addition'''
    # Implements abstract 'compute' method.
    def compute(self) -> Number:
        return addition(self.a, self.b)

# It inherits from the Calculation class and must implement the abstract method 'compute'.
class Subtraction(Calculation):
    '''subtraction'''
    # Implements abstract 'compute' method.
    def compute(self) -> Number:
        return subtraction(self.a, self.b)

# It inherits from the Calculation class and must implement the abstract method 'compute'.
class Multiplication(Calculation):
    '''multiplication'''
    # Implements abstract 'compute' method.
    def compute(self) -> Number:
        return multiplication(self.a, self.b)

# It inherits from the Calculation class and must implement the abstract method 'compute'.
class Division(Calculation):
    '''division'''
    # Implements abstract 'compute' method.
    def compute(self) -> Number:
        if self.b == 0:
            # if dividing by 0, raise error
            raise ZeroDivisionError("Division by Error is not allowed.")
        return division(self.a, self.b)
    