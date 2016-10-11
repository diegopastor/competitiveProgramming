y = input()
year = str(int(y)+1)
def isValid(num):
    if len(num) == len(''.join(set(num))):
        return True
    else:
        return False

while isValid(year) == False:
    year = str(int(year)+1)

print(year)
