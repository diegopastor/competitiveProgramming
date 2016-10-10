s = input()
su = ''.join(set(s))
if len(su) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
