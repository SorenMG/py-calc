"""Module to solve an expression"""
from sympy import solve as __solve


def solve(expr, symbol):
    """
    Solves an expression

    Args:
        expr: the expression to solve
        symbol: the symbol to solve for

    Returns:
        A solved expression
    """
    return __solve(expr, symbol)
