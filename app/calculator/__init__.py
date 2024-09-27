'''importing functions from app.operations'''
from app.operations import addition, subtraction, multiplication, division

class Calculator:

    @classmethod
    def create(cls):
        return cls()

    def add(self, a, b):
        '''Addition'''
        return addition(a,b)

    def subtract(self, a, b):
        '''Subtraction'''
        return subtraction(a,b)

    def multiply(self, a, b):
        '''Multiplication'''
        return multiplication(a,b)

    def divide(self, a, b):
        '''Division'''
        return division(a,b)
