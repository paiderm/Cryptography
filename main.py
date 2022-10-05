from Methods.Old.VigenereCipher import VigenereCipher


def main():
    print("Welcome to the Crypography Toolbox")
    print("Enter a Method to use: ")

    print("\tVigenere Cipher")

    userMethodChoice = input()

    if userMethodChoice.lower().replace(' ', '') == 'vigenerecipher':
        vigenereCipher = VigenereCipher()
        vigenereCipher.getChoice()


if __name__ == "__main__":
    main()