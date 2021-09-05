#https://atcoder.jp/contests/abc145/tasks/abc145_d
def nCr(n,r,m=10**9+7):
    re=1
    for i in range(r):
        re*=n-i
        re%=m
        re*=pow(i+1,-1,m)
        re%=m
    return re
X,Y=map(int,input().split())
if (X+Y)%3!=0:
    print(0)
    exit()
n=(X+Y)//3
if n//2-abs(X-Y)//2<0:
    print(0)
else:
    print(nCr(n,n//2-abs(X-Y)//2))