import sys                                                                  
 
def main():
    for line in sys.stdin:
        nums = line.strip().split(' ')
        nums = [n for n in nums if not n == '']

if __name__ == '__main__':
    main()
