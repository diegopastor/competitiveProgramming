input()
s = input()
n = 0

if s[0] == '>' and s[-1] == '<':
    print(0)
else:
    while '><' in s:
        s = s.replace('><', '')

    print(len(s))
