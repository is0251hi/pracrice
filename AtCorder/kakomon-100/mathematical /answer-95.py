a,b,k=map(int, input().split())
if a+b<=k:
    print(0,0)
elif a<k:
    b-=(k-a)
    a=0
    print(a,b)
else:
    a-=k
    print(a,b)
