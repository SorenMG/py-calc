"""Module for evaluating the integral"""
from sympy import integrate as __integrate


def indefiniteIntegral(expr, symbol):
    """
    Find the indefinite integral

    Args:
        expr: the expression to integrate
        symbol: the symbol to integrate with respect to

    Returns:
        The indefinite integral
    """
    return __integrate(expr, symbol)


def definiteIntegral(expr, symbol, start, end):
    """
    Finds the definite integral

    Args:
        expr: the expression to integrate
        symbol: the symbol to integrate with respect to
        start: the start of the definite integral
        end: the end of the definite integral

    Returns:
        The definite integral
    """
    return __integrate(expr, (symbol, start, end))
