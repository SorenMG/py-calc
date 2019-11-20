import pytest
from parser.parser import sympify
from sympy.parsing.sympy_parser import parse_expr


def test_sympify():
    answer = parse_expr("3*x*y**2")

    """Test normal sympy syntax"""
    expr = sympify("3*x*y**2")
    assert expr == answer

    """Test implicit multiplication"""
    expr = sympify("3xy**2")
    assert expr == answer

    """Test xor"""
    expr = sympify("3xy^2")
    assert expr == answer
