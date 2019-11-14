import fuckit
from sympy import integrate as __integrate
from ..parser import parser
from ..printer import printer

@fuckit
def integrate(input, start=0, end=0):
    symbols = input.free_symbols

    # Try to integrate
    # Indefinite integral
    if len(symbols) <= 1:
        printer.printAnswer('Indefinite integral', __integrate(input))
    else:
        # Partial integrals
        for symbol in symbols:
            printer.printAnswer('Partial integral with regard to ' + str(symbol), __integrate(input, symbol))

        integrated = input
        for symbol in symbols:
            integrated = __integrate(input, symbol)
        printer.printAnswer('Mixed partial integral', integrated)

    # Definite integral
    # if start != 0 and end != 0:
    for symbol in symbols:
        printer.printAnswer('Definite integral', __integrate(input, (symbol, start, end)))
