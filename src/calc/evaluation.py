import fuckit
from ..parser import parser
from ..printer import printer

@fuckit
def eval(input):
    parsed = parser.parseEvaluation(input)

    # Try to find evaluation
    printer.printAnswer('Evaluation', parsed[0].evalf())