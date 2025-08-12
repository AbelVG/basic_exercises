print("This script returns the triangular number for the number provided, which is" \
"the sum of the numbers in the range from 1 to the provided number")

numberProvided = int(input("Provide a number to calculate its triangular number: "))
accumulator = 0

def triangularNumberCalculator(numberProvided, accumulator):
    for i in range(1, numberProvided+1):
        accumulator = i + accumulator
    
    return accumulator

print("The triangular number for " + str(numberProvided) + " is " + str(triangularNumberCalculator(numberProvided, accumulator)))