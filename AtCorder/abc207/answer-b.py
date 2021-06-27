a,b,c,d=map(int, input().split())
if d*c-b<=0:
    print(-1)
else:
    import math
    l=a/(c*d-b)
    print(math.ceil(l))
