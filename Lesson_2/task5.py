inputListNumbers = input("Input your list s: ")
listNumbers = list(map(int, inputListNumbers.split(","))) # Get each element and translating it into type "int"

listNumbers.sort() # sorting numbers list

smallestNumber = listNumbers[0] # Get the smallest number
largestNumber = listNumbers[-1] # Get the largest number
sumNumbers = sum(listNumbers[1:-1]) # Get sum of all other numbers

print(f"The smallest number is: {smallestNumber};\nThe largest number is: {largestNumber};\nSum of all other numbers: {sumNumbers};")