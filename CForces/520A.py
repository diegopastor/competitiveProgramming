import string

input()
s = input()
s = s.lower()
s = ''.join(sorted((set(s))))
alph = string.ascii_lowercase
if s == alph:
    print('YES')
else: 
    print('NO')




