from math import ceil
import datetime
h, m = [int(x) for x in input().split(' ')]
hunger, hincrease, costOfBun, hdecrease = [float(x) for x in input().split(' ')]


if(h >= 20):
    print(ceil(hunger / hdecrease) * (costOfBun * .80))
else:
    v = datetime.timedelta(hours=20) - datetime.timedelta(hours=h,minutes=m)
    minsToEight = ceil(v.seconds / 60)
    hungerAtEight = hunger + (hincrease * minsToEight)

    BuyNoWait= ceil(hunger / hdecrease) * costOfBun
    BuyWait = ceil(hungerAtEight / hdecrease) * (costOfBun * .80)
    print(min(BuyNoWait,BuyWait))
