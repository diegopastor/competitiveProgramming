#Need to change romToInt so that 'IIV' returns -1 instead of 5 (1 + 4)
import re

a = dict()
b = dict()
a['IV'] = 4
a['IX'] = 9
a['XIV'] = 14
a['XIX'] = 19 
a['XXIV'] = 24 
a['XXIX'] = 29 
b['X'] = 10
b['V'] = 5
b['I'] = 1

def dicOfRomansTo(n):
    units=("", "I", "II", "III",  "IV", "V",
           "VI", "VII", "VIII", "IX")
    tens=("", "X", "XX", "XXX", "XL", "L",
           "LX", "LXX", "LXXX", "XC")
    dicR = {}
    for number in range(n):
        ten, unit = divmod(number, 10)
        dicR[number] = tens[ten] + units[unit]
    return dicR
    
def romToInt(roman):
    s = 0
    for key in a:
        if key in roman:
            roman = re.sub(key,'',roman)
            s = s+a[key]
    for key in b:
        s+=roman.count(key) * b[key]
    return s

def intToRom(num):
    dicOfR = dicOfRomansTo(num+1)
    return dicOfR[num] 

def dateEncryption(date):
    date = intToRom(date)
    print("date 1: %s") %date
    date = date[::-1]
    print("date 2: %s") %date
    if romToInt(date):
        return romToInt(date)
    else: 
        return -1
    
