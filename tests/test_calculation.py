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

def test_addition(a, b, expected):
    '''Test for addition operation'''
    operation = Addition.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Addition: {a} + {b} = {expected}"
    assert repr(operation) == f"Addition(a={a}, b={b}, result={expected})"

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

def test_subtraction(a, b, expected):
    '''Test for subtraction operation'''
    operation = Subtraction.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Subtraction: {a} - {b} = {expected}"
    assert repr(operation) == f"Subtraction(a={a}, b={b}, result={expected})"

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

def test_multiplication(a, b, expected):
    '''Test for multiplication operation'''
    operation = Multiplication.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Multiplication: {a} * {b} = {expected}"
    assert repr(operation) == f"Multiplication(a={a}, b={b}, result={expected})"

# parameters to test division
@pytest.mark.parametrize("a, b, expected", [
    (6,2,3),            # simple division
    (6,6,1),            # dividing same number
    (-1,-1, 1),         # dividing negatives
    (20000,200,100),    # dividing large positives
    (-100,10,-10),      # dividing one negative, one positive
    (0.5, 0.5, 1),    # dividing floats
    (-0.5, 0.5, -1),  # dividing one -float, one +float
])

def test_division(a, b, expected):
    '''Test for division operation'''
    operation = Division.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Division: {a} / {b} = {expected}"
    assert repr(operation) == f"Division(a={a}, b={b}, result={expected})"

# parameters to test division by 0
@pytest.mark.parametrize("a, b", [
    (1,0),            # divide by 0
    (100,0),          # divide by 0 with larger numbers
])

def test_division_by_zero_exception(a,b):
    '''Test for division by zero exception'''
    operation = Division.create(a,b)
    with pytest.raises(ZeroDivisionError):
        operation.compute()

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
        operation.create(a, b)
