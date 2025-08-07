#Analyze to words to determine if they're anagrams (Words that contain the same letters).
print("This script will ask you for two words and tell you if they're anagrams")
wordOne = input('Enter word number 1: ')
wordTwo = input('Enter word number 2: ')

def anagramAnalyzer(wordOne, wordTwo):
    one = sorted(wordOne.lower().replace(" ", ""))
    two = sorted(wordTwo.lower().replace(" ", ""))
    
    return one == two

print(anagramAnalyzer(wordOne, wordTwo))