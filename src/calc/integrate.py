import fuckit
from sympy import integrate as __integrate
from ..parser import parser
from ..printer import printer

def __integrateOrder(input, order):
    for _ in range(0, order):
        input = __integrate(input)
    return input

@fuckit
def integrate(input):
    parsed = parser.parseIntegral(input)

    # Try to integrate
    # Indefinite integral
    printer.printAnswer('Indefinite integral', __integrate(*parsed))

    # Partial integrals
    for symbol in parsed[0].free_symbols:
        printer.printAnswer('Partial integral with regard to ' + str(symbol), __integrate(parsed[0], symbol))

    # Mixed partial integral
    if len(parsed[0].free_symbols) == 2:
        integral = parsed[0]
        for symbol in parsed[0].free_symbols:
            integral = __integrate(integral, symbol)
        
        printer.printAnswer('Mixed partial integral, ' + str(parsed[0].free_symbols), integral)


    # Definite integral
    printer.printAnswer('Definite integral', __integrate(parsed[0], (parsed[1], parsed[2], parsed[3])))

    # Find integral of order
    printer.printAnswer('Integral of order ' + str(parsed[1]), __integrateOrder(parsed[0], parsed[1]))