print("This script receives an integer and will evaluate if it's a prime number or not")

numberProvided = input("Please provide an integer : ")

def primeNumberEvaluation(numberProvided):
    if int(numberProvided) == 1:
        return False
    elif int(numberProvided) % 2 == 0:
        return False
    else:
        return True
    
print("Is the number provided prime? " + str(primeNumberEvaluation(numberProvided)))