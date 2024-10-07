'''importing abstract methods, unions, operations and number type alias'''
from abc import ABC, abstractmethod
from app.operations import addition, subtraction, multiplication, division, Number

class Calculation(ABC):
    '''
    abstract calculation class, subclasses must inherit
    compute, __str__, and __repr__ methods
    '''
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
        pass
    @abstractmethod
    def __str__(self) -> str:
        '''
        abstract method returning string
        returned str = formatted string of the operation'''
        # No implementation here, subclasses will provide it.
        pass
    @abstractmethod
    def __repr__(self) -> str:
        '''
        abstract method returning representation for debugging
        returned str: detailed representation of operation'''
        pass

# It inherits from the Calculation class and must implement the abstract method 'compute'.
class Addition(Calculation):
    '''addition'''
    # Implements abstract compute, __str__, and __repr__ method.
    def compute(self) -> Number:
        return addition(self.a, self.b)
    def __str__(self) -> str:
        return f"Addition: {self.a} + {self.b} = {self.compute()}"
    def __repr__(self) -> str:
        return f"Addition(a={self.a}, b={self.b}, result={self.compute()})"

# It inherits from the Calculation class and must implement the abstract method 'compute'.
class Subtraction(Calculation):
    '''subtraction'''
    # Implements abstract compute, __str__, and __repr__ method.
    def compute(self) -> Number:
        return subtraction(self.a, self.b)
    def __str__(self) -> str:
        return f"Subtraction: {self.a} - {self.b} = {self.compute()}"
    def __repr__(self) -> str:
        return f"Subtraction(a={self.a}, b={self.b}, result={self.compute()})"

# It inherits from the Calculation class and must implement the abstract method 'compute'.
class Multiplication(Calculation):
    '''multiplication'''
    # Implements abstract compute, __str__, and __repr__ method.
    def compute(self) -> Number:
        return multiplication(self.a, self.b)
    def __str__(self) -> str:
        return f"Multiplication: {self.a} * {self.b} = {self.compute()}"
    def __repr__(self) -> str:
        return f"Multiplication(a={self.a}, b={self.b}, result={self.compute()})"

# It inherits from the Calculation class and must implement the abstract method 'compute'.
class Division(Calculation):
    '''division'''
    # Implements abstract compute, __str__, and __repr__ method.
    def compute(self) -> Number:
        if self.b == 0:
            # if dividing by 0, raise error
            raise ZeroDivisionError("Division by Error is not allowed.")
        return division(self.a, self.b)
    def __str__(self) -> str:
        result = self.compute()
        # if result is a whole number / int, cast to int
        # # if the number isn't a wholenumber, keep it as a float
        # we do this because during testing the computed result is always a float
        # even if its a whole number, which leads to assert errors
        formatted_result = int(result) if result.is_integer() else result
        return f"Division: {self.a} / {self.b} = {formatted_result}"
    def __repr__(self) -> str:
        result = self.compute()
        formatted_result = int(result) if result.is_integer() else result
        return f"Division(a={self.a}, b={self.b}, result={formatted_result})"
    