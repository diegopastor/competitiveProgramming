table = []
values = {'Q':9,'R':5,'B':3,'N':3,'P':1,'q':-9,'r':-5,'b':-3,'n':-3,'p':-1}
res = 0

for i in range(8):
    line = [x for x in input() if x != '.' and x != 'k' and x != 'K']
    if line:
        table.append(line)

for line in table:
    for piece in line:
        res += values[piece]

if res == 0:
    print('Draw')
elif res > 0: 
    print('White')
else:
    print('Black')
