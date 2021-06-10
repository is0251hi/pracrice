import sys
n = int(sys.stdin.readline())
t = list(map(int, input().split()))
dp=1
for x in t:
    dp|=dp<<x
 
ans=10**18
sumt=sum(t)
t.sort()
for i in range(sumt//2,sumt+1):
    if (dp>>i)&1:
        ans=min(ans,max(i,sumt-i))
        print(ans)
        break