import sys
from collections import deque
n=int(sys.stdin.readline())
tree={i:deque() for i in range(1,n+1)}
queue=deque()
seen=[0]*(n+1)
ans=[0]*(n+1)
distance=1
for _ in range(n):
    u,k,*v_l=map(int,sys.stdin.readline().split())
    for v in v_l:
        tree[u].append(v)
def bfs():
    queue.append(1)
    seen[1]=1
    while queue:
        idx=queue.popleft()
        for _ in range(len(tree[idx])):
            tree_idx=tree[idx].popleft()
            if seen[tree_idx]==0:
                seen[tree_idx]=1
                queue.append(tree_idx)
                ans[tree_idx]=ans[idx]+1
bfs()
for i,a in enumerate(ans[1:]):
    if i+1>1 and a==0:
        print(i+1,-1)
    else:
        print(i+1,a)
