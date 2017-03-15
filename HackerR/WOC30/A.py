n,t = [int(x) for x in input().split(' ')]
c = input().split(' ')
c = [int(x) for x in c]
fn = n

AddedC = 0
for candy in range(len(c)-1):
    fn -= c[candy]
    if fn < 5:
        AddedC += n - fn
        fn += n - fn
    
print(AddedC)
