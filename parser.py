class Parser:
    def isoperator(self, char):
        if char == '+' or char == '-' or char == '*' or char == '/':
            return True
        return False


    def parse(self, inputEquation):
        parsedEquation = inputEquation
        # Insert *
        # Shitty fix
        timesImmuted = 0
        for i in range(0, len(inputEquation)):
            if inputEquation[i].isalpha():
                if self.isoperator(inputEquation[i-1]):
                    continue
                # Create new string as python strings are immutable
                parsedEquation = parsedEquation[:i+timesImmuted] + '*' + parsedEquation[i+timesImmuted:]
                timesImmuted += 1

        # Insert ** as eksponent
        parsedEquation = parsedEquation.replace('^','**')

        return parsedEquation
    

if __name__ == "__main__":
    print(Parser().parse('3xt-3+y^3'))