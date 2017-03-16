import itertools
n = int(input())

vow = ['a','e','i','o','u']
con = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

def gP(n,w,a,b):
    if len(w) == n:
        print(w)
    else:
        for element in a:
            gP(n,w + element,b,a)

gP(n,'',vow,con)
gP(n,'',con,vow)
