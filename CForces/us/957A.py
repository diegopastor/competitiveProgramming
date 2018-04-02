input()
s = input()

def check(s):
    for i in range(1,len(s)-1):
        if s[i] == '?':
            if s[i-1] != '?' and s[i+1] != '?' and s[i-1] != s[i+1]:
                return False
    return True    

if 'MM' in s or 'YY' in s or 'CC' in s:
    print('No')
else:
    if(check(s)):
        print('Yes')
    else:
        print('No')
