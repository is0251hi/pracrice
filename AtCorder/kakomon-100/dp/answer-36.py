n,capacity=map(int,input().split())
items=[]
dp=[0]*(capacity+1)
for _ in range(n):
    v,w=map(int,input().split())
    items.append((v,w))
for idx,item in enumerate(items):
    v=item[0]
    w=item[1]
    for j in range(w,capacity+1):
        dp[j]=max(dp[j-w]+v, dp[j])
print(max(dp))