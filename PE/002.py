
fibs = [0,1]

[fibs.append(fibs[-2]+fibs[-1]) for i in xrange(60)]
sum = 0
for i in fibs:
    if i % 2 == 0 and i < 4000000:
        sum = sum + i

print sum
