s = input()
h = 'hello'

for char in s:
    if not len(h):
        break
    if char == h[0]:
        h = h[1:]
if not len(h):
    print('YES')
else:
    print('NO')
