import pytest
from calc.integrate import indefiniteIntegral, definiteIntegral
from parser.parser import sympify

expr = "3x"
symbol = sympify("x")

y_expr = "3xy"
y_symbol = sympify("y")


def test_indefiniteIntegral():
    """Test primitive indefinite integral"""
    answer = sympify("3x^2/2")
    assert indefiniteIntegral(expr, symbol) == answer

    """Test partial integral"""
    answer = sympify("3xy^2/2")
    assert indefiniteIntegral(y_expr, y_symbol) == answer

    """Test indefinite integral of 2'nd order"""
    answer = sympify("x^3/2")
    assert indefiniteIntegral(expr, symbol, 2) == answer


def test_definiteIntegral():
    """Test primitive definite integral"""
    start = sympify("0")
    end = sympify("10")
    answer = sympify("150")
    assert definiteIntegral(expr, symbol, start, end) == answer

    """Test partial definite integral"""
    answer = sympify("150x")
    assert definiteIntegral(y_expr, y_symbol, start, end) == answer

    """Test definite integral with variable as bound"""
    end = sympify("a")
    answer = sympify("3a^2/2")
    assert definiteIntegral(expr, symbol, start, end) == answer
