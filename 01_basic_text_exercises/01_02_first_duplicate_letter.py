
#request a string
print("this script analyzes the entered script and returns the first duplicate letter")
stringProvided = input("Provide a string: ")


#Remove empty spaces
string_no_spaces = stringProvided.replace(" ", "")
#Convert string to lower case
cleanString = string_no_spaces.lower()
#Create a buffer where characters go to wait to be compared
charList = []

#Define function to scroll through the string and add letters to the list if they're not already there
#Or just return and print them if they are found
def duplicate_scanner(string_no_spaces):

    for char in cleanString:
        if char in charList:
            return char
        else:
            charList.append(char)

print("Duplicate letter located: " + duplicate_scanner(string_no_spaces))    




        
        
