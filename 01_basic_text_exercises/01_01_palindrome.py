chosenWord = input("Enter a word: ")

def is_palindrome(chosenWord):
    lowercaseWord = chosenWord.lower()
    noSpacesWord = lowercaseWord.replace(" ", "")
    return noSpacesWord == noSpacesWord[::-1]

print(is_palindrome(chosenWord))