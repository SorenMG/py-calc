"""Module for evaluating the integral"""
from sympy import integrate as __integrate
from parser.parser import sympify


def indefiniteIntegral(expr, symbol, order=1, parse=True):
    """
    Find the indefinite integral

    Args:
        expr: the expression to integrate
        symbol: the symbol to integrate with respect to
        order: the order of the integral to find. Defaults to 1
        parse: if the expression should be parsed to sympy

    Returns:
        The indefinite integral
    """
    if parse:
        expr = sympify(expr)
        symbol = sympify(symbol)

    for _ in range(1, order):
        expr = __integrate(expr, symbol)
    return __integrate(expr, symbol)


def definiteIntegral(expr, symbol, start, end, parse=True):
    """
    Finds the definite integral

    Args:
        expr: the expression to integrate
        symbol: the symbol to integrate with respect to
        start: the start of the definite integral
        end: the end of the definite integral
        parse: if the expression should be parsed to sympy

    Returns:
        The definite integral
    """
    if parse:
        expr = sympify(expr)
        symbol = sympify(symbol)

    return __integrate(expr, (symbol, start, end))
