print("This script uses the bubble sort algorithm to sort the numbers provided")

numberList = []

def requestInput():
    keepAdding = "y"
    while keepAdding == "y":
        numberList.append(int(input("Add an int number to the list: ")))
        keepAdding = input("do you want to add another number to the list? y/n ")

def bubbleSort(numberList):
    l = len(numberList)
    for i in range(l):
        for j in range(0,l-i-1):
            if numberList[j] > numberList[j+1]:
                holder = numberList[j]
                numberList[j] = numberList[j+1]
                numberList[j+1] = holder
    return numberList


requestInput()
print("Sorted numbers list: ", bubbleSort(numberList))