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

# Gets a string as such: '{$} from {$} to {$}' and outputs the {$} as a list of parsed sympy objects
def _parsePattern(equation, pattern, willParse):
    # First get keywords from pattern
    keywords = pattern.split('{$}')

    # Remove empty indekses
    itemsDeleted = 0
    for i in range(0, len(keywords)):
        if keywords[i - itemsDeleted] == '':
            del keywords[i - itemsDeleted]
            itemsDeleted += 1

    regexString = ""

    # Strip keywords from whitespace and create regexString
    for i in range(0, len(keywords)):
        keywords[i] = keywords[i].replace(" ", "")
        regexString += keywords[i]
        if i != len(keywords) - 1:
            regexString += '|'
    
    # Find variables in equation with keywords
    variables = re.split(regexString, equation)

    # Parse variables
    if willParse:
        for i in range(0, len(variables)):
            variables[i] = _parse(variables[i])

    return variables

def parseEquation(equation):
    separator = config['separator']
    parsedEquation = _parsePattern(equation, '{$}' + separator + '{$}', True)

    symbols = parsedEquation[0].free_symbols
    # A variable was not specified in a equation with more than one variable
    if len(parsedEquation) != 2 and len(symbols) > 1:
        raise ValueError('Cannot solve a multivariable equation without a specified variable')
    elif len(symbols) < 1:
        raise ValueError('Cannot solve a set of numbers')
    elif len(parsedEquation) == 1:
        parsedEquation.append(symbols.pop())

    return parsedEquation

# Returns None if failed
def parseDefiniteIntegral(equation):
    startKeyword = config['integral']['start']
    toKeyword = config['integral']['separator']

    parsedEquation = _parsePattern(equation, '{$}' + startKeyword + '{$}' + toKeyword + '{$}', False)

    # Parse integral
    tempHolder = parseEquation(parsedEquation[0])
    del parsedEquation[0]
    
    parsedEquation.insert(0, tempHolder[1])
    parsedEquation.insert(0, tempHolder[0])
    for i in range(2, len(parsedEquation)):
        parsedEquation[i] = _parse(parsedEquation[i])

    # Not definite integral
    if len(parsedEquation) <= 2:
        return None

    return parsedEquation

def parseEvaluation(equation):
    parsedEquation = _parse(equation)