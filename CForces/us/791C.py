n,k = [int(x) for x in input().split(' ')]
answers = input().split(' ')

namelist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Ab','Ac','Ad','Ae','Af','Ag','Ba','Bb','Bc','Bd','Bx','By','Bz','Ca','Cb','Cc','Cx','Cy','Cz','Da','Db','Dc','De','Dg','Dh','Dv','Dw','Dx','Dy','Dz','Ta','Te','Ti','To','Tu','Ty','Tx','Ty','Tz','Qa','Qe','Qi','Qo']

info = namelist[:n]
start = 0

for ans in answers:
    if ans == 'NO':
        if info[start:start+k][-1] != info[start:start+k][-2] and info[start:start+k][0] != info[start:start+k][1]:
            info[start+k-1] = info[start+k-2]
    start += 1         

print(' '.join(info))
