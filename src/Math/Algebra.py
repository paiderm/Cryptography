# Convert between equivalent representations for a group isomorhpic to Z/len(alphabet) over addition
def convertBetweenLetterAndNumber(entry, alphabet):
    if type(entry) == int:
        return alphabet[entry]
    elif type(entry) == str:
        return alphabet.index(entry)