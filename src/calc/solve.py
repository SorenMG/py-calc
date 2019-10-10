import fuckit
from ..parser import parser
from ..printer import printer
from sympy import solve as __solve

@fuckit
def solve(input):
    parsed = parser.parseSolve(input)

    for symbol in parsed[0].free_symbols:
        printer.printAnswer('Solve for ' + str(symbol), __solve(parsed[0], symbol))