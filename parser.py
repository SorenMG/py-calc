# Equation Parser Module
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, split_symbols, convert_xor, factorial_notation, convert_equals_signs

transformations = (standard_transformations + (implicit_multiplication_application,) + (split_symbols,) + (convert_xor,) + (factorial_notation,) + (convert_equals_signs,))

def parse(equation):
    equation = equation.replace(" ", "")
    # Split to isolate variable
    equation = equation.split(',')
    # Parse the equation
    for i in range(0, len(equation)):
        equation[i] = parse_expr(equation[i], transformations=transformations)

    # If no variable parsed, return none
    if len(equation) != 2:
        equation.append(None)

    return equation