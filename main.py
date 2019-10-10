import cmd
from src.calc import integrate, evaluation, derivative, solve

class CalcShell(cmd.Cmd):
    prompt = '>> '
    file = None

    # Solve equation for the given variable
    def do_solve(self, input):
        """Solves the given equation.\n
        Definition:
        solve equation, variable
        """
        solve.solve(input)

    # Integrate equation for the given variable
    def do_int(self, input):
        """Integrates the given equation.\n
        Definition:
        integrate equation, variable
        """
        # Parse and integrate input
        integrate.integrate(input)

    # Find the derivative of an equation for a given variable
    def do_diff(self, input):
        """Finds the derivative of a given equation.\n
        Definition:
        diff equation
        """
        # Parse and find derivative
        derivative.diff(input)

    def do_eval(self, input):
        """Find the value of the given equation.\n
        Definition:
        eval equation
        """
        # Parse and find evaluation
        evaluation.eval(input)

    def do_wolf(self, input):
        """Calculate the equation 'wolfram-like'"""
        # Try everything
        solve.solve(input)
        integrate.integrate(input)
        derivative.diff(input)
        evaluation.eval(input)
            
if __name__ == '__main__':
    CalcShell().cmdloop()