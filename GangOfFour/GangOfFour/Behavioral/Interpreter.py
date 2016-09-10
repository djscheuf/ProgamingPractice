__author__ = 'DJS'
"""
Intent: Given a language, define a representation for its grammar along with an interpreter that uses the
representation to interpret sentences in the language.

It would appear that a common usage of Interpreter is as a polish notation calculator, or in XML parsing.
"""



class BasicArithmeticInterpepter():
    def __init__(self):
        pass

    def Parse(self,expression):
        values = []
        actions=[]

        tokens = expression.split(' ')

        for token in tokens:
            if token.isdigit():
                values.append(int(token))
            else:
                actions.append(token)

        for action in actions:
            if(action == "+"):
                temp = values.pop(0)
                temp += values.pop(0)
                values.insert(0,temp)
            elif(action == "-"):
                temp = values.pop(0)
                temp -= values.pop(0)
                values.insert(0,temp)

        print("Results: ")
        print(values)


def demonstrate():
    interpreter = BasicArithmeticInterpepter()

    interpreter.Parse("3 + 5 - 2")

if __name__ == "__main__":
    demonstrate()