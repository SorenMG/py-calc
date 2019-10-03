import cmd, sys
from sympy.solvers import solve
from sympy import Symbol
from colors import *
import os

# Integrate
# Derivative
# Solve

class CalcShell(cmd.Cmd):
    intro = 'If confused, type "help" before a command'
    prompt = 'Calc >> '
    file = None

    def printEquation(self, eq):
        sys.stdout.write(GREEN)
        print('\n')
        for e in eq:
            print(e)
            print('\n')
        sys.stdout.write(RESET)

    # Prints out commands
    def do_help(self, args):
        print(' - Solve:', self.do_solve.__doc__)

    # Solve equation for x
    def do_solve(self, arg):
        """Solves the given equation"""
        # Get variable to solve for
        arg.replace(" ", "")
        argData = arg.split(',')
        solvedEq = ""
        if len(argData) == 2:
            print(argData)
            solvedEq = solve(argData[0], Symbol(argData[1]))
        else:
            solvedEq = solve(argData[0])
         
        self.printEquation(solvedEq)

if __name__ == '__main__':
    CalcShell().cmdloop()