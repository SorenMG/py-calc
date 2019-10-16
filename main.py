import cmd
from src.calc import integrate, evaluation, derivative, solve

class CalcShell(cmd.Cmd):
    prompt = '>> '

    def emptyline(self):
        pass 
    def onecmd(self, line):
        """Calculate the equation 'wolfram-like'"""
        # Try everything
        solve.solve(line)
        integrate.integrate(line)
        derivative.diff(line)
        evaluation.eval(line)
            
if __name__ == '__main__':
    CalcShell().cmdloop()
