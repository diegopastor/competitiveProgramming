pos = input()

if 'a' in pos or 'h' in pos or '1' in pos or '8' in pos:
    if pos == 'a8' or pos == 'h8' or pos == 'a1' or pos == 'h1':
        print(3)
    else:
        print(5)
else:
    print(8)
