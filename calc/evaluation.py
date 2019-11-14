import fuckit
from ..parser import parser
from ..printer import printer

@fuckit
def eval(input):
    # Try to find evaluation
    printer.printAnswer('Evaluation', input.evalf())
