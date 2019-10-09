import fuckit
from ..parser import parser
from ..printer import printer
from sympy import diff as __diff

@fuckit
def diff(input):
    parsed = parser.parseDerivative(input)

    # Try do find derivative
    # Derivative
    printer.printAnswer('Derivative', __diff(*parsed))