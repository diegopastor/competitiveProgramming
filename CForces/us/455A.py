n = int(input())
nums = [int(x) for x in input().split(' ')]
nums.sort(reverse=True)
score = 0

def n_of_dels(n):
    return nums.count(n+1) + nums.count(n-1)

nums_dels = {x:n_of_dels(x) for x in set(nums)}
print(nums_dels)
def n_with_less_dels(dic):
    minDels = 99999999
    for num in dic:
        if dic[num] <= minDels:
            minDels = dic[num]
            numWithMinDels = num 
    return numWithMinDels

while nums:
    nwld = n_with_less_dels(nums_dels)
    if nwld in nums:
        nums.remove(nwld)
        if nwld-1 in nums:
            nums.remove(nwld-1)
        elif nwld+1 in nums:
            nums.remove(nwld+1)
        score += nwld
    else:
        del nums_dels[nwld]

print(score)
