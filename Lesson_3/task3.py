inputString = input()
symbolsList = {}

def symbolsCount(string, resultList, position):
    if len(string) > position:
        try:
            resultList[string[position].lower()] += 1
        except:
            resultList.setdefault(string[position].lower(), 1)

        return symbolsCount(string, resultList, position + 1)
    else:
        return resultList

symbolsCount(inputString, symbolsList, 0)
print(symbolsList)
