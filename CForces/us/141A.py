s = input()
s2 = input()
s3 = input()

pile = ''.join(sorted(s3))
original = ''.join(sorted(s + s2))

if pile == original:
    print('YES')
else:
    print('NO')
