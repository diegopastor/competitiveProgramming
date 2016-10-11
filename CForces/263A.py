import sys                                                                  
 
def main():
    y = 0
    for line in sys.stdin:
        nums = line.strip().split(' ')
        nums = [int(n) for n in nums if not n == '']
        if 1 in nums:
            x = nums.index(1)
            j = y
            x = abs(x-2)
            y = abs(y-2)
            print(x+y)
            break
        y += 1

if __name__ == '__main__':
    main()
