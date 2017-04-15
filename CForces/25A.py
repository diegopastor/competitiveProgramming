n = input()
nums = [int(x) for x in input().split(' ')]
evens = 0
odds = 0
last_even = None
last_odd = None

for num in nums:
    if num % 2 == 0:
        evens += 1
        last_even = num
    else:
        odds += 1
        last_odd = num

if evens == 1:
    print(nums.index(last_even)+1)
else:
    print(nums.index(last_odd)+1)
