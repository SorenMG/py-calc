"""Module for finding the derivative of a given expression"""
from sympy import diff as __diff

# TODO
# Normal derivative
# Derivative of order
# Critical points?


def derivative(expr, symbol, order=1):
    """
    Finds the derivative

    Args:
        expr: the expression to evaluate
        symbol: the symbol to evaluate with respect to
        order: order of the derivative

    Returns:
        An evaluated derivative

    """
    return __diff(expr, symbol, order)
