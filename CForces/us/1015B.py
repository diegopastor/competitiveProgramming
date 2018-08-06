n = int(input())
s = input()
t = input()

moves = []

def swap(s,i):
    s = list(s)
    s[i], s[i+1] = s[i+1], s[i]
    return ''.join(s)

if sorted(s) != sorted(t):
    print(-1)
else:
    while s != t:
        for i in range(n-1):
            if s[i] == t[i]:
                continue
            else:
                if s[i] == s[i+1]:
                    continue
                else:
                    s = swap(s,i)
                    moves.append(i+1)
    print(len(moves))
    print(*moves, sep=' ')
