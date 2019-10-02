from cmd import Cmd

class Calc(Cmd):
    promt = '>> '

    def do_help(self, arg):
        print('Help incomming')
        return True
    
if __name__ == '__main__':
    Calc().cmdloop()