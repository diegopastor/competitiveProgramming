s = input()

if len(set(s)) == 1:
    print('No')
elif len(set(s)) == 2:
    if(s.count(list(set(s))[0]) > 1 and s.count(list(set(s))[1]) > 1):
        print('Yes')
    else:
        print('No')
elif len(set(s)) == 3:
    if any(s.count(x) > 1 for x in set(s)):
        print('Yes')
    else:
        print('No')
elif len(set(s)) == 4:
    print('Yes')
else:
    print('No')
