inputNumber = int(input("Input your number: "))
currentNumber = inputNumber

while inputNumber > 0:
    # output result string
    outputResult= ""

    # create pattern for current number
    while currentNumber > 0:
        outputResult += f"{currentNumber} "
        currentNumber -= 1

    inputNumber-=1
    currentNumber = inputNumber

    print(outputResult)
