input()
s = input()
moves = 0
while 'RR' in s or 'GG' in s or 'BB' in s:
    if 'RR' in s:
        pos = s.index('RR')
        s = s[:pos] + s[(pos+1):]
        moves += 1
    if 'GG' in s:    
        pos = s.index('GG')
        s = s[:pos] + s[(pos+1):]
        moves += 1
    if 'BB' in s:
        pos = s.index('BB')
        s = s[:pos] + s[(pos+1):]
        moves += 1
print(moves)
