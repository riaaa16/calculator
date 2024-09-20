'''My Calculator Test'''
import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition():
    '''Addition function'''
    assert addition(1,1) == 2

def test_subtraction():
    '''Subtraction function'''
    assert subtraction(1,1) == 0

def test_multiplication():
    '''Multiplication function'''
    assert multiplication(2,2) == 4

def test_division():
    '''Division function'''
    assert division(2,2) == 1

def test_division_by_zero_exception():
    '''Division function testing that dividing by 0 throws an exception'''
    with pytest.raises(ZeroDivisionError):
        division(10,0)
        