#Generate all prime numbers up to the one provided by the user.
#Show the list of prime numbers, total ammount of prime numbers,
# addition and mean, biggest and smallest.
#Use matplotlib to illustrate

def isPrime(num):
    prime = False
    if num == 1 or num == 2 or num % 2 != 0:
        prime = True
    elif num % 2 == 0:
        prime = False
    return prime

def primeCount(num):
    primesList = []
    for number in range(1, num):
        if isPrime(number) == True:
            primesList.append(number)

    print("--------------------------------------\
          \nTotal amount of prime numbers: " + str(len(primesList)) + ". \nList of prime numbers: \n")
    for i in primesList:
        print(i)
    return primesList

def primeAnalysis(primesList):
    primeSum = 0
    for i in primesList:
        primeSum = primeSum + i
    print("\nSum of all prime numbers in the range: ", primeSum)
    print("mean :", primeSum/len(primesList))
    print("lowest prime: " + str(primesList[0]) + "\nHighest prime: " + str(primesList[-1]) +\
                         "\n--------------------------------------")
    
def primesPlot(primesList: list[int]) -> None:
    if not primesList:
        return
    try:
        import matplotlib.pyplot as plt
        x = list(range(1, len(primesList) + 1))
        y = primesList
        plt.figure()
        plt.scatter(x,y)
        plt.title("Prime Numbers")
        plt.xlabel("Index")
        plt.ylabel("Prime Values")
        plt.tight_layout()
        plt.show()
    except ImportError:
        pass

def main():
    try:
        primeLimit = int(input("Provide a number and this script will identify all the prime numbers before it: "))
    except ValueError:
        print("Please enter a valid Integer.")
        return

    primesList = primeCount(primeLimit)
    primeAnalysis(primesList)
    primesPlot(primesList)

if __name__ == "__main__":
    main()