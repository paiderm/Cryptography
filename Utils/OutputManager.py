class OutputManager:
    def __init__(self):
        pass

    def printAddingTwoLines_Vigenere(self, message, key):
        print()
        print("  ", end='')
        for i in range(len(message)):
            print(message[i], end='  ')

        print("\n+ ", end='')

        for i in range(len(message)):
            print(key[i % len(key)], end='  ')

        print()

    def printStepBeingTaken(self, step):
        print()
        print("STEP: " + step)
        print()

    def printIdea(self, idea):
        print()
        print("IDEA: " + idea)
        print()

    def displayConversion(self, old, new):
        print()
        for i in range(len(old)):
            print(old[i], end='   ')

        print("\t===>\t", end='')

        for i in range(len(new)):
            print(new[i], end='   ')

        print()