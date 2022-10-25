inputListString = input().replace(" ", "")
listString = inputListString.split(",") # splitting string
listString = list(set(listString)) # remove repeated values

print(listString)