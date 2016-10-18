import sys                                                                  
 
def main():
    for line in sys.stdin:
        nums = line.strip().split(' ')
        nums = [int(n) for n in nums if not n == '']
        priceOfBanana = nums[0]
        money  = nums[1]
        bananasToBuy = nums[2]
        moneyToBorrow = 0

        while money > 0:
            money -= priceOfBanana
            priceOfBanana *= 2
            bananasToBuy -= 1

        while bananasToBuy > 0:
            moneyToBorrow += priceOfBanana
            priceOfBanana *= 2
            bananasToBuy -= 1

        print(moneyToBorrow)

if __name__ == '__main__':
    main()
