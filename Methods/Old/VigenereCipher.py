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
        self.inputMessage = self.inputManger.getMessage(self.choice, self.alphabet)

        self.key = self.inputManger.getKey(self.choice, self.alphabet)

        # display the words + words
        self.outputManager.printIdea("We can \"add\" the letters of the message and the key together to get the encrypted message")
        self.outputManager.printAddingTwoLines_Vigenere(self.inputMessage, self.key)

        # convert this group to the isometric group Z/n where n is the amount of characters in the alphabet
        self.outputManager.printStepBeingTaken("Convert the message and key to the isometric group Z/n where n is the amount of characters in the alphabet")
        message_to_numbers_array = self.convertStringToNumbersModulo(self.inputMessage, self.alphabet)
        keyToNumbersArray = self.convertStringToNumbersModulo(self.key, self.alphabet)

        self.outputManager.displayConversion(self.inputMessage, message_to_numbers_array)
        self.outputManager.displayConversion(self.key, keyToNumbersArray)
        
        self.outputManager.printAddingTwoLines_Vigenere(message_to_numbers_array, keyToNumbersArray)


    def decrypt(self):
        pass

    
