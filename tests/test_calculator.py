import pytest
from app.calculator import Calculator
from app.calculation import Addition, Subtraction, Multiplication, Division

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize("operation_class, a, b, expected_result", [
    (Addition, 3, 4, 7),
    (Subtraction, 10, 4, 6),
    (Multiplication, 3, 5, 15),
    (Division, 10, 2, 5)
])
def test_operations(calculator, operation_class, a, b, expected_result):
    operation = operation_class(a, b)
    result = calculator.perform_operation(operation)
    assert result == expected_result
    assert len(calculator.get_history()) == 1

def test_history(calculator):
    operation1 = Addition(1, 2)
    operation2 = Subtraction(5, 3)
    calculator.perform_operation(operation1)
    calculator.perform_operation(operation2)
    history = calculator.get_history()
    assert len(history) == 2
    assert history[0].operation.a == 1
    assert history[1].operation.a == 5

def test_undo(calculator):
    operation1 = Addition(1, 2)
    calculator.perform_operation(operation1)
    last_command = calculator.undo()
    assert last_command is not None
    assert last_command.operation.a == 1
    assert len(calculator.get_history()) == 0

def test_clear_history(calculator):
    operation1 = Addition(1, 2)
    operation2 = Subtraction(5, 3)
    calculator.perform_operation(operation1)
    calculator.perform_operation(operation2)
    calculator.clear_history()
    assert len(calculator.get_history()) == 0
