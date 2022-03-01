"""Testing the Calculator"""
from calculator.operations import Operations





def test_calculator_result_property():
    """Testing the Calculator"""
    calc1 = Calculator()
    calc2 = Calculator()
    calc1.result = 5
    calc2.result = 6
    assert calc1.result == 5
    assert calc2.result == 6


def test_calculator_add_method():
    """Testing the Calculator"""

    assert Operations.add(1,1) == 2

def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""

    assert Operations.subtract(1,1) == 0

def test_calculator_multiply_method():
    """Testing the Calculator Subtract"""

    assert Operations.multiply(1,1) == 1
