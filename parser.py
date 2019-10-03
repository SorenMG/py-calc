# Equation Parser Module

def isoperator(char):
    if char == '+' or char == '-' or char == '*' or char == '/':
        return True
    return False


def parse(inputEquation):
    parsedEquation = inputEquation
    # Insert *
    # Shitty fix
    timesImmuted = 0
    for i in range(1, len(inputEquation)):
        if inputEquation[i].isalpha():
            if isoperator(inputEquation[i-1]):
                continue
            # Create new string as python strings are immutable
            parsedEquation = parsedEquation[:i+timesImmuted] + '*' + parsedEquation[i+timesImmuted:]
            timesImmuted += 1

    # Insert ** as eksponent
    parsedEquation = parsedEquation.replace('^','**')

    return parsedEquation