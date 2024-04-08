
print("Input phrase: ")
phrase = ''

print("You entered: " + phrase)

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
newPhrase = " "

for char in phrase:
    if char.islower():  
        newChar = alphabet[(alphabet.index(char) + 5) % 26] 
        newPhrase += newChar
    elif char.isupper():  
        newChar = alphabet[(alphabet.index(char) + 5) % 52 + 26]  
        newPhrase += newChar
    else:
        newPhrase += char 




print("The Cipher Phrase is" + newPhrase)