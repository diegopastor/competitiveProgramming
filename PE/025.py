def fib_to(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

fibs = fib_to(5000) 

for fib in fibs:
    if len(str(fib)) >= 1000:
        print(fibs.index(fib))
        break
