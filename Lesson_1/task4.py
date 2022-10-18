import math
import re

# 3x^2 - 10x + 3
# 4x^2 + 21x + 5
# x^2 - 2x - 3
equation = input("Input your quadratic equation ( For test: 3x^2 - 10x + 3): ")

# quadratic equation calculate function
def quadraticEquation(num1: int, operator1: str, num2: int, operator2: str, num3: int):
    # set arguments symbol
    if operator1 == '-': num2 = -num2
    if operator2 == '-': num3 = -num3

    # calculate a discriminant
    discriminant = (num2 ** 2) - (4 * num1 * num3)

    # search discriminant values
    if discriminant > 0:
        result1 = ((-num2 + math.sqrt(discriminant)) / num1 * 2) / 4
        result2 = ((-num2 - math.sqrt(discriminant)) / num1 * 2) / 4
        result = f"Quadratic equation resualt: X1 = {result1}; X2 = {result2}"
    elif discriminant == 0:
        result = f"Quadratic equation resualt: X = {(-num2 / (num1 * 2)) / 4}"
    elif discriminant < 0:
        result = "Equation does not exist!"
    else:
        result = "Equation invalid!"

    return result

# remove unnecessary elements of the equation
try:
    pattern = ['*', '^2', 'x', '(', ')']
    for i in range(0, len(pattern)):
        equation = equation.replace(pattern[i], '')

    # get everything element from equation
    equationArguments = re.split(r'\s+', equation)

    equationResualt = quadraticEquation(int(equationArguments[0]), equationArguments[1], int(equationArguments[2]),
                                        equationArguments[3], int(equationArguments[4]))
    print(equationResualt)
except:
    print("Equation invalid!")