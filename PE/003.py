num = 600851475143
primes = [x for x in range(3,13000,2) 
        if all (x % y != 0 for y in range(2,x))]

for prime in primes:
    if num % prime == 0:
        ans = prime
print(ans)
