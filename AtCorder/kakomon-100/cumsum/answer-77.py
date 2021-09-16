import sys
input = sys.stdin.buffer.readline
n,m=map(int,input().split())
dist=[int(input()) for _ in range(n-1)]
move=[int(input()) for _ in range(m)]
cum_sum=[0]*n
for i,d in enumerate(dist):
    cum_sum[i+1]=cum_sum[i]+d
ans=0
idx=0
for mv in move:
    ans+=abs(cum_sum[mv+idx]-cum_sum[idx])
    idx+=mv
print(ans%10**5)