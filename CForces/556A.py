l = int(input())
s = input()
d = {'1':0,'0':0}
for char in s:
    d[char] += 1

if d['1'] == d['0']:
    print(0)
else:
    print(l-(2*(min(d['1'],d['0']))))
