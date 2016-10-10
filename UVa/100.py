def inpar(n):
    return (3 * n) + 1

def par(n):
    return n/2



def serie(n):
    counter = 0
    if n == 1:
        return counter
    elif n % 2 != 0:
        n = inpar(n)
        counter = counter + 1
        return serie(n)
    elif n % 2 == 0:
        n = par(n)
        counter = counter + 1
        return serie(n)

print serie(10)
