n = int(input())
nums = input().split(' ') 
nums = [int(x) for x in nums]
i = 0
subarray = 1
ans = 1

while i+1 < len(nums):
    if nums[i] < nums[i+1]:
        subarray += 1
    else:
        ans = max(ans,subarray)
        subarray = 1 
    i += 1

print(max(ans,subarray))
    
