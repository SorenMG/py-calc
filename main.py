import cmd, sys
from sympy import *
from sympy import Symbol
from colors import *
import re
import parser

class CalcShell(cmd.Cmd):
    intro = 'If confused, type "help" before a command'
    prompt = 'Calc >> '
    file = None

    def printEquation(self, eq):
        sys.stdout.write(GREEN)
        print('\n')
        print(eq)
        print('\n')
        sys.stdout.write(RESET)

    def processInput(self, eq):
        eq = re.sub(r"\s+", "", eq)
        # Split to isolate variable
        eq = eq.split(',')
        # Parse the equation
        eq[0] = parser.parse(eq[0])
        return eq

        
    # Prints out commands
    def do_help(self, args):
        print(' - Solve:', self.do_solve.__doc__)

    # Solve equation for the given variable
    def do_solve(self, arg):
        """Solves the given equation.\n
        Definition:
        solve equation, variable
        """
        # Get variable to solve for
        argData = self.processInput(arg)
        if len(argData) == 2:
            self.printEquation(solve(argData[0], Symbol(argData[1]))[0])
        else:
            self.printEquation(solve(argData[0])[0])

    # Integrate equation for the given variable
    def do_integrate(self, arg):
        """Integrates the given equation.\n
        Definition:
        integrate equation, variable
        """
        argData = self.processInput(arg)
        if len(argData) == 2:
            self.printEquation(integrate(argData[0], Symbol(argData[1])))
        else:
            self.printEquation(solve(argData[0]))

    # Find the derivative of an equation for a given variable
    def do_diff(self, arg):
        """Finds the derivative of a given equation.\n
        Definition:
        diff equation
        """
        argData = self.processInput(arg)
        if len(argData) == 2:
            self.printEquation(diff(argData[0], Symbol(argData[1])))
        else:
            self.printEquation(diff(argData[0]))
            

if __name__ == '__main__':
    CalcShell().cmdloop()