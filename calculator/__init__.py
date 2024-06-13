from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
    
class Calculator:
    history = []

    @staticmethod
    def add(a, b):
        calculation = Calculation(a, b, add)
        Calculator.history.append(calculation)
        return calculation.get_result()

    @staticmethod
    def subtract(a, b):
        calculation = Calculation(a, b, subtract)
        Calculator.history.append(calculation)
        return calculation.get_result()
    
    @staticmethod
    def multiply(a, b):
        calculation = Calculation(a, b, multiply)
        Calculator.history.append(calculation)
        return calculation.get_result()
    
    @staticmethod
    def divide(a, b):
        calculation = Calculation(a, b, divide)
        Calculator.history.append(calculation)
        return calculation.get_result()

    @staticmethod
    def clear_history():
        Calculator.history.clear()

    @staticmethod
    def get_history():
        return Calculator.history
