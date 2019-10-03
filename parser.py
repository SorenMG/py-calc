# Equation Parser Module
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, split_symbols, convert_xor, factorial_notation

def parse(inputEquation):
    transformations = (standard_transformations + (implicit_multiplication_application,) + (split_symbols,) + (convert_xor,) + (factorial_notation,))
    
    # Insert all from the right of the = sign on the left
    if (inputEquation.find('=') != -1):
        splittedEq = inputEquation.split('=')
        inputEquation = splittedEq[0] + '-(' + splittedEq[1] + ')'

    return parse_expr(inputEquation, transformations=transformations)