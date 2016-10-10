size = int(input())

ss = [[i] for i in range(size)]
while True:
    instruction = input()
    if 'quit' in instruction:
        break
    a, b = map(int, instruction.split()[1::2])
    if 'move' in instruction and len(ss[a]) > 1:
        for x in ss[a][1:]:
            ss[x] = [x]
    if 'onto' in instruction and len(ss[b]) > 1:
        for x in ss[b][1:]:
            ss[x] = [x]
    ss[b] += ss[a]
    ss[a] = []


for i in range(len(ss)):
    print (i,": ",end="")
    if not ss[i]:
        print()
        continue
    for x in ss[i][:-1]:
        print (x, end=" ")
    print(ss[i][-1]) 
