class Cipher:
    def __init__(self):
        self.inputMessage = ''
        self.outputMessage = ''
        self.key = ''
        self.choice = ''
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijkmlnopqrstuvwxyz'

        self.getChoice()

    def getChoice(self):
        print("Enter E to Encrypt or D to Decrypt")
        self.choice = input().upper()

    def isValidMessage(self, message):
        for i in message:
            if self.alphabet.find(i) < 0:
                return False
        return True
