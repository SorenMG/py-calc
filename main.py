import cmd, sys
from sympy import solve, Derivative, init_printing, Integral, pprint, integrate, diff, Symbol, evalf
from colors import *
import parser

class CalcShell(cmd.Cmd):
    prompt = '>> '
    file = None
    init_printing()

    def parse(self, eq):
        return parser.parseEquation(eq)

    def parseDefIntegral(self, eq):
        return parser.parseDefiniteIntegral(eq)

    def parseEval(self, eq):
        return parser.parseEvaluation(eq)

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

        answer = solve(parsedInput, variable)

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
        # Try to parse as definite integral
        if (self.parseDefIntegral(input) != None):
            parsedInput, variable, startRange, endRange = self.parseDefIntegral(input)

            # Calculate answer
            answer = integrate(parsedInput, (variable, startRange, endRange))
            prettyInput = Integral(parsedInput, (variable, startRange, endRange))
            return prettyInput, answer

        # Parse as indefinite integral
        parsedInput, variable = self.parse(input)

        prettyInput = Integral(parsedInput, variable)
        answer = integrate(parsedInput, variable)
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

        prettyInput = Derivative(parsedInput, variable)
        answer = diff(parsedInput, variable)

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

    def _eval(self, input):
        parsedInput = self.parseEval(input)
        answer = parsedInput.evalf()
        return parsedInput, answer

    def do_eval(self, input):
        """Find the value of the given equation.\n
        Definition:
        eval equation
        """
        try:
            # Parse and evaluate input
            parsedInput, answer = self._eval(input)

            self.printEquation(parsedInput, answer)
        except ValueError as e:
            self.printError(e)
            
if __name__ == '__main__':
    CalcShell().cmdloop()