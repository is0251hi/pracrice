n,capacity=map(int,input().split())
items=[]
dp=[[0]*(capacity+1) for _ in range(len(items)+1)]
for _ in range(n):
    v,w=map(int,input().split())
    items.append((v,w))
for idx,item in enumerate(items):
    for capa in range(capacity+1):
        privious=dp[idx][capa]
        if item[1]>capa or items[idx-1]>capa:
            dp[idx+1][capa]=privious
        else:
            