n,w=map(int,input().split())
items=[]
dp=[[0]*(w+1) for _ in range(n+1)]
for i in range(n):
    v,w=map(int,input().split())
    items.append((v,w))

for idx,item in enumerate(items):
    for capacity in range(w+1):
        previous_item_value=dp[idx][capacity]
        weight=item[1]
        if capacity>=weight:
            value_item_weight=dp[idx][capacity-weight]
            value=item[0]
            dp[idx+1][capacity]=max(value_item_weight+value,previous_item_value)
        else:
            dp[idx+1][capacity]=previous_item_value
print(dp)
ans=[]
capacity=w
for i in range(len(items),0,-1):
    if dp[i-1][capacity]!=dp[i][capacity]:
        ans.append(items[i-1])
        capacity-=items[i-1][1]
print(ans)