n,max_capacity=map(int,input().split())
items=[]
dp=[[0]*(max_capacity+1) for _ in range(n+1)]
for i in range(n):
    v,w=map(int,input().split())
    items.append((v,w))

for idx,item in enumerate(items):#重さごとに一つ前の商品と選択した商品を比較して最大のアイテムに更新し続けている
    for capacity in range(max_capacity+1):
        previous_item_value=dp[idx][capacity]
        weight=item[1]
        if capacity>=weight:
            value_item_weight=dp[idx][capacity-weight]
            value=item[0]
            dp[idx+1][capacity]=max(value_item_weight+value,previous_item_value)
        else:
            dp[idx+1][capacity]=previous_item_value
ans=0
capacity=max_capacity
for i in range(len(items),0,-1):
    if dp[i-1][capacity]!=dp[i][capacity]:
        ans+=(items[i-1][0])
        capacity-=items[i-1][1]
print(ans)