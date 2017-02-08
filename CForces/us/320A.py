mn = input()

def magic(n):
    for char in n: 
        if char not in ('4','1'):
            return False
    if n[0] != '1' or '444' in n:
        return False
    return True

if magic(mn):
    print('YES')
else:
    print('NO')
