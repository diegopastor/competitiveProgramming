s = input()

if 'h' in s:
    i = s.index('h')
    if 'e' in s:
        j = s.index('e')
        if j > i:
            if 'l' in s:
                i = s.index('l')
                if i > j:
                    if 'l' in s[i:]:
                        j = s[i:].index('l')
                        if j > i:
                            if 'o' in s:
                                i = s.index('o')
                                if i > j:
                                    print('YES')
else:
    print('NO')

