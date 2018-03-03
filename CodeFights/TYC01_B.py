def digitDegree(n):
    ans = 0
    while(True):
        if(len(str(n)) == 1):
            return ans
        ans += 1
        digits = [int(x) for x in str(n)]
        n = sum(digits)
        if(len(str(n)) == 1):
            return ans
