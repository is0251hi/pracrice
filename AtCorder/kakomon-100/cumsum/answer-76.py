n=int(input())
a_l=list(map(int,input().split()))
cumsum=[0]*(len(a_l)+1)
for i in range(len(a_l)):
    cumsum[i+1] = cumsum[i] + a_l[i]
def calc(n):
    ans=0
    for i in range(len(cumsum)-n):
        diff = cumsum[i+n] - cumsum[i]
        ans = max(diff,ans)
    return ans
for j in range(1,n+1):
    print(calc(j))