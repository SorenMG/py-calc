"""Module for finding the derivative of a given expression"""
from sympy import diff as __diff
from parser.parser import sympify

# TODO
# Normal derivative
# Derivative of order
# Critical points?


def derivative(expr, symbol, order=1, parse=True):
    """
    Finds the derivative

    Args:
        expr: the expression to evaluate
        symbol: the symbol to evaluate with respect to
        order: order of the derivative
        parse: if the expression should be parsed to sympy

    Returns:
        An evaluated derivative

    """
    if parse:
        expr = sympify(expr)
        symbol = sympify(symbol)

    return __diff(expr, symbol, order)
