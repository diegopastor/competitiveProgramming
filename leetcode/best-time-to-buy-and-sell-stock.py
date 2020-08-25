from math import inf


def maxProfit(prices):
    minimum = inf
    maximum = 0
    for price in prices:
        if price < minimum:
            minimum = price
        else:
            maximum = max(maximum, price - minimum)
    return maximum



print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([1,2]))
