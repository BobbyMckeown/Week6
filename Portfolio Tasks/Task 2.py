def findFactors():
    print("The factors are: \n")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)


number = int(input("Enter a Number: "))
print(findFactors())
