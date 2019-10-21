import cmd
import sys
from src.calc import integrate, evaluation, derivative, solve
from src.parser import parser

class WolfShell(cmd.Cmd):
    prompt = '>> '

    def emptyinput(self):
        pass
    def onecmd(self, input):
        """Calculate the equation 'wolfram-like'"""
        input = parser.parseEquation(input)
        # Try everything
        if len(input) <= 1:
            input = input[0]
            solve.solve(input)
            integrate.integrate(input)
            derivative.diff(input)
            evaluation.eval(input)
        else:
            pass

if __name__ == '__main__':
    WolfShell().cmdloop()
