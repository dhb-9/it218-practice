from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.operations import add
from calculator import Calculator

### init.py test
def test_addition():
    calculation = Calculation(Decimal('5'), Decimal('5'), add)
    assert calculation.get_result() == Decimal('10')


## calculation.py test
def test_calculator_add():
    assert Calculator.add(Decimal('5'), Decimal('5')) == Decimal('10')

def test_calculator_subtract():
    assert Calculator.subtract(Decimal('5'), Decimal('5')) == Decimal('0')

def test_calculator_multiply():
    assert Calculator.multiply(Decimal('5'), Decimal('5')) == Decimal('25')

def test_calculator_divide():
    assert Calculator.divide(Decimal('5'), Decimal('5')) == Decimal('1')

def test_calculator_divideby0():
    with pytest.raises(ValueError, match="Can't divide by 0"):
        Calculator.divide(Decimal('5'), Decimal('0'))


## history test
def test_history(): ## looked up
    Calculator.clear_history()
    Calculator.add(1, 1)
    Calculator.subtract(5, 2)
    history = Calculator.get_history()
    assert len(history) == 2
    assert isinstance(history[0], Calculation)
    assert isinstance(history[1], Calculation)
    assert history[0].get_result() == 2
    assert history[1].get_result() == 3

def test_clear_history():
    Calculator.clear_history()
    Calculator.add(1, 1) == 2
    Calculator.clear_history()
    assert len(Calculator.history) == 0
