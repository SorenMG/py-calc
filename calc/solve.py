import fuckit
from ..parser import parser
from ..printer import printer
from sympy import solve as __solve

@fuckit
def solve(input):
    for symbol in input.free_symbols:
        printer.printAnswer('Solve for ' + str(symbol), __solve(input, symbol))
