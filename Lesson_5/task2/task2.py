from flask import Flask, render_template, request

application = Flask("Calculator")

def calculate(number1: int, number2: int, operation: str):
    match operation:
        case "+":
            result = number1 + number2
        case "-":
            result = number1 - number2
        case "*":
            result = number1 * number2
        case "/":
            result = number1 / number2
        case "**":
            result = number1 ** number2
        case "root":
            result = number1 ** (1 / number2)
        case _:
            result = "NaN"
    return result

@application.route("/")
def start():
    try:
        if request.method == "GET":
            firstNumber = int(request.args.get("first_num"))
            secondNumber = int(request.args.get("second_num"))
            operation = request.args.get("operation")
    except:
        firstNumber = 0
        secondNumber = 0
        operation = "+"
    return render_template("index.html", result=calculate(firstNumber, secondNumber, operation))


application.run(host="0.0.0.0", port=8081)