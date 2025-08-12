print("This script calculates the factorial for a provided integer")

numberProvided = int(input("Please provide an integer to calculate it's factorial: "))
accumulator = 1

def factorialCalculator(numberProvided, accumulator):
    rangeEnd = numberProvided + 1
    for i in range(1, rangeEnd):
        accumulator = i * accumulator
    
    return accumulator

print("The factorial for " + str(numberProvided) + " is " + str(factorialCalculator(numberProvided, accumulator)))