import sys

def main():
    for line in sys.stdin:
        nums = line.strip().split(' ')                                     
        nums = [n for n in nums if not n == '']
        n = int(nums[0])
        m = int(nums[1])
        a = int(nums[2])
        amount = ((m+a-1)//a)*((n+a-1)//a)
        print(amount)

if __name__ == '__main__':
    main()

