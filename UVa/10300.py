import sys

def main():
    input = []
    for line in sys.stdin:
        nums = line.strip().split(' ')
        nums = [n for n in nums if not n == '']
        testcases = int(nums[0])
            
    for case in range(testcases):
        farmers = nums[0]
        for farmer in range(farmers):
            nums.remove(farmers)
            squareMts = int(nums[0])
            animals = int(nums[3])
            w = animals / squareMts
            e = int(nums[4])
            p = w * e 
            tp = p * animals 
        

if __name__ == '__main__':
    main()
