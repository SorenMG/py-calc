import fuckit
from sympy import integrate as __integrate
from ..parser import parser
from ..printer import printer

# @fuckit
def integrate(input):
    symbols = input.free_symbols

    # Try to integrate
    # Indefinite integral
    if len(symbols) <= 1:
        printer.printAnswer('Indefinite integral', __integrate(input))
    else:
        # Partial integrals
        for symbol in symbols:
            printer.printAnswer('Partial integral with regard to ' + str(symbol), __integrate(input, symbol))

    # Definite integral


    # Mixed partial integral
    # if len(input[0].free_symbols) == 2:
        # integral = input[0]
        # for symbol in input[0].free_symbols:
            # integral = __integrate(integral, symbol)
        
        # printer.printAnswer('Mixed partial integral, ' + str(input[0].free_symbols), integral)


    # Definite integral
    # printer.printAnswer('Definite integral', __integrate(input[0], (input[1], input[2], input[3])))

    # Find integral of order
    # printer.printAnswer('Integral of order ' + str(input[1]), __integrateOrder(input[0], input[1]))

