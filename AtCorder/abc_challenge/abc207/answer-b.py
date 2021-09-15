a,b,c,d=map(int, input().split())
if c*d<=b:
    print(-1)
else:
    import math
    l=a/(c*d-b)
    print(math.ceil(l))
