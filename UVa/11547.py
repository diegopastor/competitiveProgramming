tc = input()
cnt = 0

def operations(n):
    return (((((n*567)/9)+7492)*235)/47)-498

while cnt != tc:
    testcase = input()
    number = operations(testcase)
    number2 = str(number)
    numberR = number2[::-1]
    print numberR[1]
    cnt = cnt + 1

