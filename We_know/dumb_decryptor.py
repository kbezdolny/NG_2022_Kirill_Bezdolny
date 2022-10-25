inputMessage = input("Your massage: ")
step = int(input("Input step (for task is 13): "))
resultMessage = ""

largeLetters =  "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallLetters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
for i in inputMessage:
    # get large letters
    largePosition = largeLetters.find(i)
    newLargePosition = largePosition + step
    # get small letters
    smallPosition = smallLetters.find(i)
    newSmallPosition = smallPosition + step

    if i in largeLetters:
        resultMessage += largeLetters[newLargePosition]
    elif i in smallLetters:
        resultMessage += smallLetters[newSmallPosition]
    else:
        resultMessage += i

print(f"Result message: {resultMessage}")