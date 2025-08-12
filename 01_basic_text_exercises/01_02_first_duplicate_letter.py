
#request a string
print("this script analyzes the entered script and returns the first duplicate letter")
stringProvided = input("Provide a string: ")


#Remove empty spaces
string_no_spaces = stringProvided.replace(" ", "")
#Convert string to lower case
cleanString = string_no_spaces.lower()
#Extract provided string's length to use as range
charList = []


def duplicate_scanner(string_no_spaces):

    for char in cleanString:
        if char in charList:
            return char
        else:
            charList.append(char)

print("Duplicate letter located: " + duplicate_scanner(string_no_spaces))    




        
        
