n = int(input())
arr = [int(x) for x in input().split(' ')]
    
ln = 1
mxln = 1
for i in range(len(arr)-1):
    if arr[i] <= arr[i+1]:
        ln += 1
    else:
        ln = 1
    mxln = max(mxln,ln)
        
print(mxln)
