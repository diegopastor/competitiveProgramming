days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
months = [32,31,29]

s1 = input()
s2 = input()

ss = days.index(s1)

if days[(ss)%7] == s2 or days[(ss)%7] == s2 or days[(ss)%7] == s2:
    print('YES')
else:
    print('NO')
