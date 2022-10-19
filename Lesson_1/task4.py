a, b, c = int(input("Input a number: ")), int(input("Input b number: ")), int(input("Input c number: "))

# calculate a discriminant
discriminant = b ** 2 - 4 * a * c

# search discriminant values
if discriminant > 0:
    x1 = (-b + discriminant ** 0.5) / (a * 2)
    x2 = (-b - discriminant ** 0.5) / (a * 2)
    result = f"Quadratic equation resualt: x1 = {x1}; x2 = {x2}"
elif discriminant == 0:
    result = f"Quadratic equation resualt: x = {-b / (a * 2)}"
elif discriminant < 0:
    result = "Equation does not exist!"
else:
    result = "Equation invalid!"

print(result)