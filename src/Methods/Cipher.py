from Utils.InputManager import InputManager
from Utils.OutputManager import OutputManager
from Math import Algebra
class Cipher:
    def __init__(self):
        self.inputMessage = ''
        self.outputMessage = ''
        self.key = ''
        self.choice = ''
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijkmlnopqrstuvwxyz'
        self.inputManger = InputManager()
        self.outputManager = OutputManager()

        self.getChoice()

    def getChoice(self):
        print("Enter E to Encrypt or D to Decrypt")
        self.choice = input().upper()

    def convertStringToNumbersModulo(self, string, alphabet):
        numbers = []
        for i in range(len(string)):
            numbers.append(Algebra.convertBetweenLetterAndNumber(string[i], alphabet))

        return numbers
