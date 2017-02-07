disks = int(input())
initial = str(input())
final = str(input())
i = 0
t = 0
for number in initial:
    t += min(abs(int(initial[i]) - int(final[i])), 10 - abs(int(initial[i]) - int(final[i])))
    i += 1
print(t)
