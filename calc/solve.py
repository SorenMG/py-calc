"""Module to solve an expression"""
from sympy import solve as __solve
from parser.parser import sympify


def solve(expr, symbol, parse=True):
    """
    Solves an expression

    Args:
        expr: the expression to solve
        symbol: the symbol to solve for
        parse: if the expression should be parsed to sympy

    Returns:
        A solved expression
    """
    if parse:
        expr = sympify(expr)
        symbol = sympify(symbol)

    return __solve(expr, symbol)[0]
