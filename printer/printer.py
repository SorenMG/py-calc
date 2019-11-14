from sympy import init_printing, pprint
from .colors import *
import sys

init_printing()

def printError(message):
    sys.stdout.write(RED)
    print('Error:', message)
    sys.stdout.write(RESET)

def printAnswer(title, answer):
    sys.stdout.write(BLUE)
    sys.stdout.write(BOLD)
    print(title)
    sys.stdout.write(GREEN)
    pprint(answer)
    sys.stdout.write(RESET)