# Equation Parser Module
from parse import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, split_symbols, convert_xor, factorial_notation, convert_equals_signs

transformations = (standard_transformations + (implicit_multiplication_application,) + (split_symbols,) + (convert_xor,) + (factorial_notation,) + (convert_equals_signs,))

def sympify(equation):
    return parse_expr(equation, transformations=transformations)

def parseEquation(input):
    patterns = [
        "{}, {}..{}",
        "{}"
    ]

    for pattern in patterns:
        if parse(pattern, input) is not None:
            # Make Result object to list
            templist = [] 
            for e in parse(pattern, input):
                e = sympify(e)
                templist.append(e)
            return templist
