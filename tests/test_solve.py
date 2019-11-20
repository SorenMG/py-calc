import pytest
from calc.solve import solve
from parser.parser import sympify


def test_solve():
    """Test primitive solve"""
    expr = "3+x=2"
    symbol = sympify("x")
    answer = sympify("-1")
    assert solve(expr, symbol) == answer
