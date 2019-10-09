import fuckit
from ..parser import parser
from ..printer import printer
from sympy import solve as __solve

@fuckit
def solve(input):
    parsed = parser.parseSolve(input)

    printer.printAnswer('Solve', __solve(*parsed))