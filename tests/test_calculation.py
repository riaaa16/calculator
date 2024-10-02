'''testing app.calculation functions'''
import pytest
from app.calculation import Addition, Subtraction, Multiplication, Division

# parameters to test addition
@pytest.mark.parametrize("a, b, expected", [
    (1,2,3),            # simple addition
    (0,0,0),            # adding zeroes
    (-1,-1,-2),         # adding negatives
    (100,200,300),      # adding large positives
    (-10,10,0),         # adding one negative, one positive
    (0.5, 0.5, 1.0),    # adding floats
    (-0.5,1.5,1.0),     # adding one -float, one +float
])

def test_addition_compute(a, b, expected):
    '''testing class and abstract methods for addition'''
    addition = Addition.create(a,b)
    # f means a formatted string literal
    assert addition.compute() == expected, f"Expected {expected}, but got {addition.compute()}"

# parameters to test subtraction
@pytest.mark.parametrize("a, b, expected", [
    (3,2,1),            # simple subtracting
    (0,0,0),            # subtracting zeroes
    (-1,-1, 0),         # subtracting negatives
    (300,200,100),      # subtracting large positives
    (-10,10,-20),       # subtracting one negative, one positive
    (1.5, 0.5, 1.0),    # subtracting floats
    (-0.5,1.5,-2.0),    # subtracting one -float, one +float
])

def test_subtraction_compute(a, b, expected):
    '''testing class and abstract methods for subtraction'''
    subtraction = Subtraction.create(a,b)
    # f means a formatted string literal
    assert subtraction.compute() == expected, f"Expected {expected}, but got {subtraction.compute()}"

# parameters to test multiplication
@pytest.mark.parametrize("a, b, expected", [
    (3,2,6),            # simple multiplication
    (0,100,0),          # multiplying zeroes
    (-1,-1, 1),         # multiplying negatives
    (100,200,20000),    # multiplying large positives
    (-10,10,-100),      # myultiplying one negative, one positive
    (0.5, 2.0, 1.0),    # multiplying floats
    (-0.5, 2.0, -1.0),  # multiplying one -float, one +float
])

def test_multiplication_compute(a, b, expected):
    '''testing class and abstract methods for multiplication'''
    multiplication = Multiplication.create(a,b)
    # f means a formatted string literal
    assert multiplication.compute() == expected, f"Expected {expected}, but got {multiplication.compute()}"

# parameters to test division
@pytest.mark.parametrize("a, b, expected", [
    (6,2,3),            # simple division
    (6,6,1),            # dividing same number
    (-1,-1, 1),         # dividing negatives
    (20000,200,100),    # dividing large positives
    (-100,10,-10),      # dividing one negative, one positive
    (0.5, 0.5, 1.0),    # dividing floats
    (-0.5, 0.5, -1.0),  # dividing one -float, one +float
])

def test_division_compute(a, b, expected):
    '''testing class and abstract methods for division'''
    division = Division.create(a,b)
    # f means a formatted string literal
    assert division.compute() == expected, f"Expected {expected}, but got {division.compute()}"

# parameters to test division by 0
@pytest.mark.parametrize("a, b", [
    (1,0),            # divide by 0
    (100,0),          # divide by 0 with larger numbers
])

def test_division_by_zero(a, b):
    '''testing division by zero'''
    division = Division.create(a,b)
    # with tells pytest to expect ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        division.compute()

# parameters to test type errors for all operations
@pytest.mark.parametrize("a, b, operation", [
    ("a", 1, Addition),            # string and Number for addition
    (None, 1, Subtraction),        # None and Number for subtraction
    ([1, 2], 1, Multiplication),    # list and Number for multiplication
    (object(), 1, Division),       # generic object and Number for division
])

def test_invalid_types(a, b, operation):
    '''pytest is expecting TypeError'''
    with pytest.raises(TypeError):
        calculation = operation.create(a, b)
