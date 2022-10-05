from Methods.Cipher import Cipher


class VigenereCipher(Cipher):
    def __init__(self):
        self.description()

        super().__init__()

        self.encrypt() if self.choice == 'E' else self.decrypt()

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

    def decrypt(self):
        pass

    def displayLayout(self, message, key):
        print()
        print("  " + str(message))

        print("+ ", end='')

        for i in range(len(message)):
            print(key[i % len(key)], end='')

        print()