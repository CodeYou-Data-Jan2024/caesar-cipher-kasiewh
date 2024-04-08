
print("Input phrase: ")
phrase = input()

print("You entered: " + phrase)

alphabet = "abcdefghijklmnopqrstuvwxyzabcde"
newPhrase = " "




for i in range(0, len(phrase)):
    try:
        char = phrase[i]
        newChar = str(alphabet[alphabet.index(char)+5])
        newPhrase += newChar
    except:
        newChar = str(alphabet[0])
        newPhrase += newChar

print("The Cipher Phrase is" + newPhrase)

