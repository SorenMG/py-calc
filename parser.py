# Equation Parser Module
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, split_symbols, convert_xor, factorial_notation, convert_equals_signs
from sympy import Eq

transformations = (standard_transformations + (implicit_multiplication_application,) + (split_symbols,) + (convert_xor,) + (factorial_notation,) + (convert_equals_signs,))

def parse(inputEquation):
    return parse_expr(inputEquation, transformations=transformations)