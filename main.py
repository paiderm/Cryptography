from Methods.Old.VigenereCipher import VigenereCipher


def main():
    print("Welcome to the Crypography Toolbox")
    print("Enter a Method to use: ")

    print("\t1) Vigenere Cipher")

    userMethodChoice = input()
    userMethodChoice = userMethodChoice.lower().replace(' ', '')
    if userMethodChoice == 'vigenerecipher' or userMethodChoice == '1':
        vigenereCipher = VigenereCipher()
        vigenereCipher.getChoice()


if __name__ == "__main__":
    main()