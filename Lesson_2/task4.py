inputNumber = int(input("Input your number: "))
factorialNumber = 1

if (inputNumber > 0):
    while inputNumber > 0:
        factorialNumber *= inputNumber
        inputNumber -= 1

    print(factorialNumber)
else:
    print("Factorial number less than zero!")
