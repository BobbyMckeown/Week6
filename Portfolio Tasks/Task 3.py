def isPrimeNumber():
    for i in range(2, number - 1):
        if number % i == 0:
            return print("This number is not a prime")

        else:
            return print("This Number is a prime")


number = int(input("Please enter a number: "))
print(isPrimeNumber())
