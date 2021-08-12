import sys
from collections import deque
n=int(sys.stdin.readline())
tree={i:deque() for i in range(1,n+1)}
ans=[0]*(n+1)
for _ in range(n):
    u,k,*v_l=map(int,sys.stdin.readline().split())
    for v in v_l:
        tree[u].append(v)
queue=[]

def bfs():
    pass
