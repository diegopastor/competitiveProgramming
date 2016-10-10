def sumSquared(nums):
    return sum(nums)**2

def squaredSum(nums):
    squared = [x ** 2 for x in nums]
    return sum(squared)

nums = [i for i in range(1,101)]
print (sumSquared(nums) - squaredSum(nums))
