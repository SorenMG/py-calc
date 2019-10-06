import cmd, sys
from sympy import solve, Derivative, init_printing, Integral, pprint, integrate, diff, Symbol
from colors import *
import parser

class CalcShell(cmd.Cmd):
    prompt = '>> '
    file = None
    init_printing()

    def parse(self, eq):
        return parser.parse(eq)

    def printEquation(self, input, answer):
        sys.stdout.write(GREEN)
        print('In :')
        pprint(input)
        sys.stdout.write(RED)
        print('Out:')
        pprint(answer)
        sys.stdout.write(RESET)

    def printError(self, message):
        sys.stdout.write(RED)
        print('Error:', message)
        sys.stdout.write(RESET)
        
    # Prints out commands
    def do_help(self, args):
        print(' - Solve:', self.do_solve.__doc__)

    # Exit shell
    def do_exit(self, args):
        exit()

    def _solve(self, input):
        parsedInput, variable = self.parse(input)

        answer = None

        if variable != None:
            answer = solve(parsedInput, variable)
        else:
            answer = solve(parsedInput)

        return parsedInput, answer

    # Solve equation for the given variable
    def do_solve(self, input):
        """Solves the given equation.\n
        Definition:
        solve equation, variable
        """
        try:
            # Parse and solve input
            parsedInput, answer = self._solve(input)

            self.printEquation(parsedInput, answer)
        except ValueError as e:
            self.printError(e)

    def _int(self, input):
        parsedInput, variable = self.parse(input)

        prettyInput = None
        answer = None

        if variable != None:
            prettyInput = Integral(parsedInput, variable)
            answer = integrate(parsedInput, variable)
        else:
            prettyInput = Integral(parsedInput)
            answer = integrate(parsedInput)
        return prettyInput, answer

    # Integrate equation for the given variable
    def do_int(self, input):
        """Integrates the given equation.\n
        Definition:
        integrate equation, variable
        """
        try:
            # Parse and integrate input
            parsedInput, answer = self._int(input)

            self.printEquation(parsedInput, answer)
        except ValueError as e:
            self.printError(e)

    def _diff(self, input):
        parsedInput, variable = self.parse(input)

        prettyInput = None
        answer = None

        if variable != None:
            prettyInput = Derivative(parsedInput, variable)
            answer = diff(parsedInput, variable)
        else:
            prettyInput = Derivative(parsedInput)
            answer = diff(parsedInput)
        return prettyInput, answer

    # Find the derivative of an equation for a given variable
    def do_diff(self, input):
        """Finds the derivative of a given equation.\n
        Definition:
        diff equation
        """
        try:
            # Parse and differentiate input
            parsedInput, answer = self._diff(input)

            self.printEquation(parsedInput, answer)
        except ValueError as e:
            self.printError(e)
            
if __name__ == '__main__':
    CalcShell().cmdloop()