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

        self.outputManager.printNote("We want to repeat the key as many times as we need in order to cover the entire plain text. If we don't there will be parts of the message that won't be encrypted.")
        # possibly ask for feedback


        # convert this group to the isometric group Z/n where n is the amount of characters in the alphabet
        self.outputManager.printStepBeingTaken("Convert the message and key to the isometric group Z/n where n is the amount of characters in the alphabet")
        message_to_numbers_array = self.convertStringToNumbersModulo(self.inputMessage, self.alphabet)
        key_to_numbers_array = self.convertStringToNumbersModulo(self.key, self.alphabet)

        self.outputManager.displayConversion(self.inputMessage, message_to_numbers_array)
        self.outputManager.displayConversion(self.key, key_to_numbers_array)
        
        self.outputManager.printIdea("Now we have numbers that we can do binary operations with like adding")

        self.outputManager.printAddingTwoLines_Vigenere(message_to_numbers_array, key_to_numbers_array)
        
        output_message_numbers_array = []
        for i in range(len(message_to_numbers_array)):
            current_message_number = message_to_numbers_array[i]
            key_idx = i % len(key_to_numbers_array)
            current_key_number = key_to_numbers_array[key_idx]
            
            current_encrypted_number = current_message_number + current_key_number

            output_message_numbers_array.append(current_encrypted_number)
        
        self.outputManager.printAddingTwoLines_Vigenere(output_message_numbers_array)

        for i in output_message_numbers_array:
            if i >= 26:
                self.outputManager.printProblem("We have numbers that are greater than or equal to 26. However, there are only 26 letters in the alphabet")
                self.outputManager.printStepBeingTaken(f"Convert our numbers to be within our range of 0 to {len(self.alphabet)} and still make sense. We can do this if we take each number and find the remainder after dividing by 26")
                [number % len(self.alphabet) for number in output_message_numbers_array]
                self.outputManager.printAddingTwoLines_Vigenere(message_to_numbers_array, key_to_numbers_array)
                self.outputManager.printAddingTwoLines_Vigenere(output_message_numbers_array)

                break


    def decrypt(self):
        pass

    
