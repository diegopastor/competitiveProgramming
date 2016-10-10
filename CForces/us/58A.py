s = input()
p = False

for char in s:
    if char == 'h':
        hI = s.index('h')
        p = True
        break

for char in s: 
    if char == 'e':
        eI = s.index('e')
        if eI > hI:
            p = True
            s = s[eI:]
            break
        else:
            p = False

if 'l' in s and 'o' in s:
    for char in s:
        LlI = s.index('l')
        LoI = s.index('o') 
    if LoI > LlI and s.count('l') >= 2:
        p = True
else:
        p = False


if p == True:
    print('YES')
else: 
    print('NO')


