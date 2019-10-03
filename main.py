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
        return eq.split(',')
        
    # Prints out commands
    def do_help(self, args):
        print(' - Solve:', self.do_solve.__doc__)

    # Solve equation for x
    def do_solve(self, arg):
        """Solves the given equation.\n
        Definition:
        solve equation, variable
        """
        # Get variable to solve for
        argData = self.processInput(arg)
        argData[0] = parser.parse(argData[0])
        solvedEq = ""
        if len(argData) == 2:
            solvedEq = solve(argData[0], Symbol(argData[1]))
        else:
            solvedEq = solve(argData[0])
         
        self.printEquation(solvedEq[0])

    def do_integrate(self, arg):
        """Integrates the given equation.\n
        Definition:
        integrate equation, variable
        """
        argData = self.processInput(arg)
        argData[0] = parser.parse(argData[0])
        solvedEq = ""
        if len(argData) == 2:
            solvedEq = integrate(argData[0], Symbol(argData[1]))
        else:
            solvedEq = solve(argData[0])
        
        self.printEquation(solvedEq)

    def do_diff(self, arg):
        """Finds the derivative for a given equation.\n
        Definition:
        diff equation
        """
        argData = self.processInput(arg)
        argData[0] = parser.parse(argData[0])
        solvedEq = ""
        if len(argData) == 2:
            solvedEq = diff(argData[0], Symbol(argData[1]))
        else:
            solvedEq = diff(argData[0])

        self.printEquation(solvedEq)
            

if __name__ == '__main__':
    CalcShell().cmdloop()