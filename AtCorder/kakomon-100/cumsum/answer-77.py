n,m=map(int,input().split())
move=[]
cum_sum=[0]*n
for i in range(n-1):
    dist=int(input())
    cum_sum[i+1]=cum_sum[i]+dist
for _ in range(m):
    move.append(int(input()))

ans=0
idx=0
for mv in move:
    ans+=abs(cum_sum[mv+idx]-cum_sum[idx])
    idx+=mv
print(ans%10**5)