number1, number2 = int(input("Input first number: ")), int(input("Input second number: "))
operation = input("Input operation ( +, -, *, /, ^, sqrt ): ")

match operation:
    case "+": result = number1 + number2
    case "-": result = number1 - number2
    case "*": result = number1 * number2
    case "/": result = number1 / number2
    case "**": result = number1 ** number2
    case "sqrt": result = number1 ** (1 / number2)
    case _: result = "NaN"

print(f"Your result: {result}")