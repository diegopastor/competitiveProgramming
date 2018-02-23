num = input()
for i in range(len(num)-1):
    if num[i] == '-' and num[i+1] == '-':
        num = list(num)
        num[i] = '2'
        num[i+1] = 'x'
        num = ''.join(num)

for i in range(len(num)-1):
    if num[i] == '-' and num[i+1] == '.':
        num = list(num)
        num[i] = '1'
        num[i+1] = 'x'
        num = ''.join(num)

num = num.replace('x','')
num = num.replace('.','0')
print(num)
