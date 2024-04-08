
phrase = input("Input phrase: ")

print("You entered: " + phrase)

alphabet = "abcdefghijklmnopqrstuvwxyz"
newPhrase = ''

phrase = phrase.lower()

for char in phrase:
    if char in alphabet:
        newChar = alphabet[(alphabet.index(char) + 5) % 26]
        newPhrase += newChar
    else:
        newPhrase += char




print("The encrypted sentence is: " + newPhrase)