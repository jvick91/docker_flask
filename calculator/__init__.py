""" This is the Calculator Class"""
from calculator.operations import Addition, Subtraction, Multiplication

class Calculator:
    """ This is the default result property"""

    @staticmethod
    def add(value_1, value_2):
        """ This is the add method"""
        return Addition.add(value_1, value_2)

    @staticmethod
    def subtract(value_1, value_2):
        """ This is the subtract method"""
        return Subtraction.subtract(value_1, value_2)

    @staticmethod
    def multiply(value_1, value_2):
        """ This is the subtract method"""
        return Multiplication.multiply(value_1, value_2)

    def get_result(self):
        """ This is the get result method"""
        return self.result
