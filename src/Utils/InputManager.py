class InputManager:
    def __init__(self):
        pass

    def getMessage(self, option, alphabet):
        prompt = "Enter the Message to " + "Encrypt: " if option.upper() == 'E' else "Decrypt: "
        inputMessage = self.continuePromptingUntilCorrect(prompt, alphabet)

        return inputMessage

    def getKey(self, option, alphabet):
        prompt = "Enter the Key to " + "Encrypt: " if option.upper() == 'E' else "Decrypt: " + "the Message"
        key = self.continuePromptingUntilCorrect(prompt, alphabet)

        return key

    def isValidMessage(self, message, alphabet):
        for i in message:
            if alphabet.find(i) < 0:
                return False
        return True

    def continuePromptingUntilCorrect(self, prompt, alphabet):
        userInput = input(prompt)
        while not self.isValidMessage(userInput, alphabet):
            print("Invalid Key")
            userInput = input(prompt)
        return userInput