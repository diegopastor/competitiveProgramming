import sys                                                                  
rooms = 0
input()

for line in sys.stdin:
    nums = line.strip().split(' ')
    nums = [int(n) for n in nums if not n == '']
    if nums[1] - nums[0] >= 2:
        rooms += 1

print(rooms)
