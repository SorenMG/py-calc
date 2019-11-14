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
        derivative = __diff(input)
        printer.printAnswer('Derivative', derivative) 
        printer.printAnswer('Critical value', __solve(derivative))
    else:
        for symbol in symbols:
            derivative = __diff(input, symbol)
            printer.printAnswer('Partial derivative with regard to ' + str(symbol), derivative)
            # Critical values
            printer.printAnswer('Critical value', __solve(derivative))
