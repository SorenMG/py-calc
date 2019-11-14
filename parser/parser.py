"""Module to parse an expression to sympy"""
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, split_symbols, convert_xor, factorial_notation, convert_equals_signs

transformations = (standard_transformations + (implicit_multiplication_application,) + (split_symbols,) + (convert_xor,) + (factorial_notation,) + (convert_equals_signs,))


def sympify(expr, allowTransformations=True):
    """
    Parse an expression to sympy

    Args:
        expr: the expression to parse
        allowTransformations: if it should parse with transformations. Defaults to true

    Returns:
        A sympy expression
    """
    if allowTransformations:
        return parse_expr(expr, transformations=transformations)
    return parse_expr(expr)
