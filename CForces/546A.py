v = input().split(' ')
priceOfBanana = int(v[0])
savings = int(v[1])
wantedBananas = int(v[2])
neededMoney = 0
priceOfCB = 0

for banana in range(1,wantedBananas+1):
    priceOfCB = banana * priceOfBanana
    neededMoney += priceOfCB

if savings >= neededMoney:
    print(0)
else:
    print(neededMoney - savings)
