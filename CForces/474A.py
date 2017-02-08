o = input()
msg = input()
abc = 'qwertyuiopasdfghjkl;zxcvbnm,./'
Dmsg = ''

if o == 'L':
    for char in msg:
        Dmsg += abc[(abc.index(char)+1)]
else:
    for char in msg:
        Dmsg += abc[(abc.index(char)-1)]
print(Dmsg)
