import sys
from math import fabs

def main():
    for line in sys.stdin:
        nums = line.strip().split(' ')
        nums = [n for n in nums if not n == '']

        a = int(nums[0])
        b = int(nums[1])
        try:
            print (int(fabs(a-b)))
        except IndexError:
            continue

if __name__ == '__main__':
    main()                
                  
