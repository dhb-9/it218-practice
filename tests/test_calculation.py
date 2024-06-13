import pytest

from calculator.calculation import Calculation
from calculator.operations import add
from calculator import Calculator

### init.py test
def test_addition():
    calculation = Calculation(5, 5, add)
    assert calculation.get_result() == 10


## calculation.py test
def test_calculator_add():
    Calculator.clear_history()
    Calculator.get_history()
    assert Calculator.add(5, 5) == 10

def test_calculator_subtract():
    assert Calculator.subtract(5, 5) == 0

def test_calculator_multiply():
    assert Calculator.multiply(5, 5) == 25

def test_calculator_divide():
    assert Calculator.divide(5, 5) == 1

def test_calculator_divideby0():
    with pytest.raises(ValueError, match="Can't divide by 0"):
        Calculator.divide(5, 0)