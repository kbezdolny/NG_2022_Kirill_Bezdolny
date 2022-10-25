inputString = input()
lettersList = {}
lettersCountList = []

# add letters and letters count to lettersList and lettersCountList
for i in range(len(inputString)):
    if inputString[i] != " ":
        try:
            lettersList[inputString[i].lower()] += 1
        except:
            lettersList.setdefault(inputString[i].lower(), 1)
        lettersCountList.append(inputString[i].lower())


# deleted all recurring letters
lettersCountList = list(set(lettersCountList))

# unsorted list
strList = ""
for i in range(len(lettersCountList)):
    strList += f"{lettersCountList[i]} - {lettersList[lettersCountList[i]]}; "
print(f"All letters list: {strList}")

# alphabetical sorted list
lettersCountList.sort()
strSortingList = ""
for i in range(len(lettersCountList)):
    strSortingList += f"{lettersCountList[i]} - {lettersList[lettersCountList[i]]}; "
print(f"Alphabetical sorted list: {strSortingList}")
