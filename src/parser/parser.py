# Equation Parser Module
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, split_symbols, convert_xor, factorial_notation, convert_equals_signs
import json
from parse import parse

# Load configuration
config = None
try:
    with open('config.json') as f:
        config = json.load(f)
except json.decoder.JSONDecodeError:
    print('Could not load JSON')
    exit()

transformations = (standard_transformations + (implicit_multiplication_application,) + (split_symbols,) + (convert_xor,) + (factorial_notation,) + (convert_equals_signs,))

def __sympify(equation):
    return parse_expr(equation, transformations=transformations)

def __parse(input, patterns):
    for pattern in patterns:
        parsed = parse(pattern, input)
        if parsed != None:
            return parsed

def parseDerivative(input):
    input.strip()

    patterns = [
        '{} order {}',
        '{}, {}',
        '{}'
    ]

    parsed = __parse(input, patterns)

    parsedList = []

    for e in parsed:
        parsedList.append(__sympify(e))

    return parsedList

def parseEvaluation(input):
    input.strip()

    patterns = [
        '{}'
    ]

    parsed = __parse(input, patterns)

    parsedList = []

    for e in parsed:
        parsedList.append(__sympify(e))

    return parsedList

def parseIntegral(input):
    input.strip()

    patterns = [
        '{}, {} from {} to {}',
        '{} order {}',
        '{}, {}',
        '{}'
    ]

    parsed = __parse(input, patterns)

    parsedlist = []

    for e in parsed:
        parsedlist.append(__sympify(e))

    return parsedlist

def parseSolve(input):
    input.strip()

    patterns = [
        '{}, {}',
        '{}'
    ]

    parsed = __parse(input, patterns)

    parsedlist = []

    for e in parsed:
        parsedlist.append(__sympify(e))

    return parsedlist