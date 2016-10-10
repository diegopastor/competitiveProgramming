import sys

def main():
    for line in sys.stdin:
        values = line.strip().split(' ')
        values = [n for n in values if not n == '']
    
        i = int(values[0])
        j = int(values[1])
        i = i * 2
        ans = i * j
        print(ans)

if __name__ == '__main__':
    main()
