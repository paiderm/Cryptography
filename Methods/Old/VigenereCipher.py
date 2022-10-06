from email import message
from Methods.Cipher import Cipher
from Math import Algebra

class VigenereCipher(Cipher):
    def __init__(self):
        self.description()

        super().__init__()

        self.encrypt() if self.choice.upper() == 'E' else self.decrypt()

    def description(self):
        what = ''
        when = ''
        how = 'This cipher works off of modular arithmetic and the fact that the alphabet is isomorphic to ' \
              'the group Z/n over addition where n is the amount of letters in the alphabet being used.'


    def encrypt(self):
        self.inputMessage = input("Enter the Message to Encrypt: ")
        while not self.isValidMessage(self.inputMessage):
            print("Invalid Message")
            self.inputMessage = input("Enter the Message to Encrypt: ")

        self.key = input("Enter the Key to Encrypt the Message: ")
        while not self.isValidMessage(self.key):
            print("Invalid Key")
            self.key = input("Enter the Key to Encrypt the Message: ")

        self.displayLayout(self.inputMessage, self.key)

        messageToNumbersArray = []
        
        for i in range(len(self.inputMessage)):
            messageToNumbersArray.append(Algebra.convertBetweenLetterAndNumber(self.inputMessage[i], self.alphabet))

        keyToNumbersArray = []
        for i in range(len(self.key)):
            keyToNumbersArray.append(Algebra.convertBetweenLetterAndNumber(self.key[i], self.alphabet))

        self.displayLayout(messageToNumbersArray, keyToNumbersArray)

    def decrypt(self):
        pass

    def displayLayout(self, message, key):
        print()
        print("  ", end='')
        for i in range(len(message)):
            print(message[i], end='  ')

        print("\n+ ", end='')

        for i in range(len(message)):
            print(key[i % len(key)], end='  ')

        print()
