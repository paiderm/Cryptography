import string


class OutputManager:
    def __init__(self):
        pass

    def printAddingTwoLines_Vigenere(self, message, key=None):
        characters_in_line = 0
        print()
        print("  ", end='')
        for i in range(len(message)):
            print(message[i], end='  ')
            if type(message[i]) == str:
                characters_in_line += 3
            elif type(message[i]) == int:
                characters_in_line += 4

        if key!= None:
            print("\n+ ", end='')
            for i in range(len(message)):
                print(key[i % len(key)], end='  ')

            
            print('\n' + '_' * characters_in_line)

        print()

    def printStepBeingTaken(self, step):
        print()
        print("STEP: " + step)
        print()

    def printIdea(self, idea):
        print()
        print("IDEA: " + idea)
        print()

    def printNote(self, note):
        print()
        print("NOTE: " + note)
        print()

    def displayConversion(self, old, new):
        print()
        for i in range(len(old)):
            print(old[i], end='   ')

        print("\t===>\t", end='')

        for i in range(len(new)):
            print(new[i], end='   ')

        print()
    
    def printProblem(self, problem):
        print()
        print("PROBLEM: " + problem)
        print()