input()
nums = [int(x) for x in input().split(' ')]
odds = [x for x in nums if x & 1]
evens = [x for x in nums if x not in odds]
