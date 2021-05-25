def metodoIndex(element, seeker) -> int:
    count = 0
    for parts in element:
        if parts == seeker:
            return count
        else:
            count += 1
    return -1


def metodoSplit(string: str, separador=" ") -> list:
    listOfTerms = []
    temp = ""
    for element in string:
        if element != separador:
            temp += element
        else:
            listOfTerms.append(temp)
            temp = ""
    if len(temp) > 0:
        listOfTerms.append(temp)
    return listOfTerms
