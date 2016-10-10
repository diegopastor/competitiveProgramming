def singleDigitGeneratedNumber(L,R):
    singleDigitNumbers = []
    total = 0
    for number in range(L,R):
        if isSingleDigit(number):
            singleDigitNumbers.append(number)
    for singleDigitNumber in singleDigitNumbers:
        total = total + int(singleDigitNumber)
    return total

def isSingleDigit(number):
    numbersList = []
    counter = 0
    number = str(number)
    for digit in number:
        numbersList.append(digit)
    firstDigit = numbersList[0] 
    for char in numbersList:
        if char == firstDigit:
            counter = counter + 1
    if counter == len(numbersList):
        return True
    else:
        return False

print (singleDigitGeneratedNumber(40,9390))
