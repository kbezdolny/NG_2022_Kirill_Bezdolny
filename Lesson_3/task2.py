def enterPersonData(text):
    return input(text)

# Sort the string function
def sortEnterString(string: str):
    wordsList = string.split(" ")
    wordsList.sort()
    return " ".join(wordsList)

# Count the number of elements function
def countElementsEnterString(string: str):
    wordsList = string.split(" ")
    return len(wordsList)

# Display only vowels or consonants function
def vowelsAndConsonantsElements(string: str, key: str):
    # vowels letters list
    vowelsLetters = "iouy"

    clearString = ""
    for letter in string:
        if letter == " ":
            clearString += letter
            continue

        match key:
            case "a":
                if letter.lower() in vowelsLetters:
                    clearString += letter
            case "b":
                if letter.lower() not in vowelsLetters:
                    clearString += letter
            case _: return "Unknown element!"
    return f"Your result: {clearString}"

# Split by words, and output words from the end function
def outputWordsFromTheEnd(words: list):
    outputList = ""
    for wordPosition in range(len(words)):
        outputList += f" {words[-(wordPosition+1)]}"
    return outputList

# Display the word by number function
def displayWordByNumber(string: str):
    wordsList = string.split(" ")
    wordNumber = int(input("Enter word number: "))
    return f"Word with number {wordNumber}: {wordsList[wordNumber - 1]}"

def outputResult():
    # get input string
    inputString = enterPersonData("Input your string: ")

    # commands list
    commandsList = "1. Sort the string\n" \
                   "2. Count the number of elements\n" \
                   "3. Display only vowels or consonants\n" \
                   "4. Split by words, and output words from the end\n" \
                   "5. Display the word by number\n" \
                   "6. Enter the line again\n" \
                   "7. Exit the program\n"
    print("\nPlease select commands:\n" + commandsList)

    # do commands
    match enterPersonData("Input command number: "):
        case "1":
            print(sortEnterString(inputString))
        case "2":
            print(countElementsEnterString(inputString))
        case "3":
            print(vowelsAndConsonantsElements(inputString, enterPersonData("Choose an option:\na) Display only vowels\nb) Display only consonants\n")))
        case "4":
            print(outputWordsFromTheEnd(inputString.split(" ")))
        case "5":
            print(displayWordByNumber(inputString))
        case "6":
            return outputResult()
        case "7":
            return print("Program shutdown!")
        case _:
            print("NaN")

outputResult()