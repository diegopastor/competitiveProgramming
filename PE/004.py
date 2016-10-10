def isPalindrome(a):
    if str(a) == str(a)[::-1]:
        return True
    else:
        return False

tDN = [x for x in range(999,99,-1)]

def biggestPal(x):
    palindromes = []
    for number in x:
        for number2 in x:
            if isPalindrome(number * number2):
                palindromes.append(number * number2)
                palindromes.sort()
                print(palindromes)

biggestPal(tDN)
