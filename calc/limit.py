from sympy import limit as __limit
from parser.parser import sympify


def limit(expr, symbol, to, dir="+", parsed=True):
    """
    Find the limit

    Args:
        expr: the expression to find the limit of
        symbol: the symbol to limit
        to: the value to limit to
        dir: "+" if it should come from positive side "-" if it should come from negative. Defaults to positive
        parsed: if the expression should be parsed

    Returns:
        What the expression limits to
    """
    if parsed:
        expr = sympify(expr)
        symbol = sympify(symbol)

    return __limit(expr, symbol, to, dir)
