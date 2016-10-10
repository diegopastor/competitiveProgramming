import sys

def main():
    for line in sys.stdin:
        num = line.strip().split(' ')
        num = [n for n in num if not n == '']
        weight = int(num[0])
        if weight % 2 == 0:
            if weight == 2:
                print('NO')
            else:
                print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()
