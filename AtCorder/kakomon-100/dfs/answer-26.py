import sys
from collections import deque
n,q=map(int,sys.stdin.readline().split())
part={i:deque() for i in range(1,n+1)}
ans=[0]*(n+1)
seen=[0]*(n+1)
stack=[]
for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    part[a].append(b)
    part[b].append(a)
for _ in range(q):
    p,x=map(int,sys.stdin.readline().split())
    ans[p]+=x
def dfs_add():
    seen[1]=1
    stack.append(1)
    while stack:
        idx=stack.pop()
        if not idx in part:
            continue
        for _ in range(len(part[idx])):
            part_idx = part[idx].popleft()
            if seen[part_idx]==0:
                seen[part_idx]=1
                ans[part_idx]+=ans[idx]
                stack.append(part_idx)
dfs_add()
print(*ans[1:])
