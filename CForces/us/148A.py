import sys                                                                  
 
def main():
    for line in sys.stdin:
        nums = line.strip().split(' ')
        nums = [int(n) for n in nums if not n == '']
        dragons = 0
        k = nums[0]
        l = nums[1]
        m = nums[2]
        n = nums[3]
        d = nums[4]
        

if __name__ == '__main__':
    main()
