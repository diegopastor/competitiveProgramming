n = input()
for i in range(int(n)):
    a,b = [int(x) for x in input().split(' ')]
    if a == b:
        print("=")
    elif max(a,b) == a:
        print(">")
    else:
        print("<")
