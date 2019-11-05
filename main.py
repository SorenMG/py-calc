import cmd
import sys
from src.calc import integrate, evaluation, derivative, solve
from src.parser import parser
from src.printer import printer

class WolfShell(cmd.Cmd):
    prompt = '>> '

    def emptyinput(self):
        pass
    def onecmd(self, input):
        """Calculate the equation 'wolfram-like'"""
        input = parser.parseEquation(input)

        printer.printAnswer('Input', input)

        # Try everything
        if len(input) <= 1:
            input = input[0]
            solve.solve(input)
            integrate.integrate(input)
            derivative.diff(input)
            evaluation.eval(input)
        # Calulate with interval
        else:
            parsed, start, end = (e for e in input)
            start = int(start)
            end = int(end)
            print(parsed, start, end)
            solve.solve(parsed)
            integrate.integrate(parsed, start, end)

if __name__ == '__main__':
    WolfShell().cmdloop()
