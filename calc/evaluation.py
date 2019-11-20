from parser.parser import sympify
"""Module for evaluating an expression"""


def evaluate(expr, parse=True):
    """
    Evaluates a given expression

    Args:
        expr: the expression to evaluate
        parse: if the expression should be parsed to sympy

    Returns:
        An evaluated expression
    """
    if parse:
        expr = sympify(expr)
    return expr.evalf()
