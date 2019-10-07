# Equation Parser Module
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, split_symbols, convert_xor, factorial_notation, convert_equals_signs
import json
import re

# Load configuration
config = None
try:
    with open('config.json') as f:
        config = json.load(f)
except json.decoder.JSONDecodeError:
    print('Could not load JSON')
    exit()

transformations = (standard_transformations + (implicit_multiplication_application,) + (split_symbols,) + (convert_xor,) + (factorial_notation,) + (convert_equals_signs,))

def _parse(equation):
    return parse_expr(equation, transformations=transformations)

def parse(equation):
    # equation = equation.replace(" ", "")
    # Split to isolate variable
    # equation = re.split(config['separator'] + '|' + config['integral']['start'], equation)'
    equation = equation.split(config['separator'])
    # Parse the equation
    for i in range(0, len(equation)):
        equation[i] = _parse(equation[i])

    # If no variable parsed, return none
    if len(equation) != 2:
        equation.append(None)

    return equation

# Returns -1 if failed
def parseDefiniteIntegral(equation):
    keyword = config['integral']['start']
    if equation.find(keyword) != -1:
        # Find limit
        limitIndex = equation.find(keyword)
        limit = equation[limitIndex + len(keyword):]

        # Find limit range
        separatorKeyword = config['integral']['separator']
        if limit.find(separatorKeyword) == -1:
            raise ValueError('Could not find limit to definite integral')

        startRange, endRange = limit.split(separatorKeyword)

        # Crop equation
        equation = equation[:limitIndex]

        # Parse equation and its variable
        parsedEquation, variable = parse(equation)

        # Parse and return equation and limits
        return parsedEquation, variable, _parse(startRange), _parse(endRange)
    # return None