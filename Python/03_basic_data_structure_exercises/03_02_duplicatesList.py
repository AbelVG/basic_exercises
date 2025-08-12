#Crear una función que permita identificar los elementos duplicados de una lista.

print("This script identifies duplicate elements in a list.")

List = []
duplicatesList = []

def requestInput():
    keepAdding = "y"
    while keepAdding == "y":
        List.append(input("Add a value to the list: "))
        keepAdding = input("do you want to add another value to the list? y/n ")

def duplicateDetector(List, duplicatesList):
    for i in List:
        if List.count(i) > 1 and i not in duplicatesList:
            duplicatesList.append(i)
            print(duplicatesList)
    return duplicatesList
requestInput()
print("Duplicates found: ", duplicateDetector(List, duplicatesList))
