#Request a string and convert it into a slug
#Remove special characters and replace spaces with dashes

print("This script takes a character string and converts it into a slug,\n removing non alphanumeric characters and swapping spaces with dashes")
textProvided = input("Please provide a character string to convert into a slug: ")

forbiddenChars = ["/", "*", "%", "\\"]

def slugify(textProvided):
    
    for char in forbiddenChars:
        textProvided = textProvided.replace(char, "")
    
    textProvided = textProvided.replace(" ", "-").lower()

    
    return textProvided
print(slugify(textProvided))