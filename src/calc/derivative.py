import fuckit
from ..parser import parser
from ..printer import printer
from sympy import diff as __diff
from sympy import solve as __solve

def __derivativeOrder(input, order, symbol):
    for _ in range(0, order):
        input = __diff(input, symbol)
    return input

@fuckit
def diff(input):
    parsed = parser.parseDerivative(input)

    # Try do find derivative
    # Partial derivative
    for symbol in parsed[0].free_symbols:
        derivative = __diff(parsed[0], symbol)
        printer.printAnswer('Partial derivative of ' + str(symbol), derivative)

        # Critical value
        parsedSolve = parser.parseSolve(str(derivative) + '=0')
        printer.printAnswer('Critical value', __solve(parsedSolve, symbol))

    # Derivative of order
    for symbol in parsed[0].free_symbols:
        printer.printAnswer('Derivative of order ' + str(parsed[1]), __derivativeOrder(parsed[0], parsed[1], symbol))
