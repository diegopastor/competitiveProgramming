s = input()

lowerC = sum(1 for char in s if char.islower())
upperC = sum(1 for char in s if char.isupper())

if lowerC == upperC:
    print(s.lower())
elif lowerC > upperC:
    print(s.lower())
else:
    print(s.upper())
