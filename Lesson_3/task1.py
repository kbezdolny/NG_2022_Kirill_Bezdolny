def inputOperation():
    operation = input("Input operation ( +, -, *, /, ^, sqrt ): ")
    return operation

def inputNumbers():
    numbers = [int(input("Input first number: ")), int(input("Input second number: "))]
    return numbers

def addNumbers(numbersList):
    return numbersList[0] + numbersList[1]

def subtractNumbers(numbersList):
    return numbersList[0] - numbersList[1]

def multiplyNumbers(numbersList):
    return numbersList[0] * numbersList[1]

def divideNumbers(numbersList):
    return numbersList[0] / numbersList[1]

def powerNumbers(numbersList):
    return numbersList[0] ** numbersList[1]

def rootNumbers(numbersList):
    return numbersList[0] ** (1 / numbersList[1])

def outputResult():
    match inputOperation():
        case "+":
            result = addNumbers(inputNumbers())
        case "-":
            result = subtractNumbers(inputNumbers())
        case "*":
            result = multiplyNumbers(inputNumbers())
        case "/":
            result = divideNumbers(inputNumbers())
        case "^":
            result = powerNumbers(inputNumbers())
        case "sqrt":
            result = rootNumbers(inputNumbers())
        case _:
            result = "NaN"
    print(f"Your result: {result}")

outputResult()