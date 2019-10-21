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
    symbols = input.free_symbols

    # Try do find derivative
    # Partial derivative
    if len(symbols) <= 1:
        printer.printAnswer('Derivative', __diff(input)) 
    else:
        for symbol in symbols:
            printer.printAnswer('Partial derivative with regard to ' + str(symbol), __diff(input, symbol))

        # Critical value
        # inputSolve = parser.parseSolve(str(derivative) + '=0')
        # printer.printAnswer('Critical value', __solve(inputSolve, symbol))
