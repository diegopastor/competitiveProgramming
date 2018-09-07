n, k = [int(x) for x in input().split(' ')]
nums = [int(x) for x in input().split(' ')]
nms = nums
kLargest = {}
problems = []

for i in range(k,0,-1):
    kLargest[nums.index(max(nums))] = max(nums)
    nums[nums.index(max(nums))] = 0
ans = sum([v for key, v in kLargest.items()])

for key in kLargest.keys():
    nms[key] = []


print(nms)
# print(ans)
# print(*problems,sep=' ')
