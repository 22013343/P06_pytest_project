import pytest
from calculator.calculator import Calculator

class TestCalculator:
    #add
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    #subtract
    def test_subtract(self):
        #arrange
        a = 5555
        b = 1234
        cal= Calculator()

        #act
        result = cal.subtract(a,b)

        # assert
        expected = 4321
        assert result == expected

    #multiply
    def test_multiply(self):
        #arrange
        a = 5555
        b = 1234
        cal= Calculator()

        #act
        result = cal.multiply(a,b)

        # assert
        expected = 6854870
        assert result == expected

    #divide 
    def test_divide(self):
        #arrange
        a = 25
        b = 5
        cal= Calculator()

        #act
        result = cal.divide(a,b)

        # assert
        expected = 5
        assert result == expected

    def test_divide_by_zero(self):
        # Arrange
        a = 25
        b = 0
        cal = Calculator()

        # Act & Assert
        with pytest.raises(ZeroDivisionError, match="Division by zero error"):
            cal.divide(a, b)