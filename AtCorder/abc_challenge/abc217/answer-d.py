import sys
from collections import deque
sys.setrecursionlimit(10**6)
l,q=map(int,sys.stdin.readline().split())
wood={0:l}
wood_key=[0]
def check(num):
    wood_key.sort()
    left=0
    right=len(wood_key)
    while left<right:
        mid=right//2
        if mid>num:
            right=mid
        else:
            left=mid+1
    a=left
    inter=(a,wood[a])
    return inter
for _ in range(q):
    c,x=map(int,sys.stdin.readline().split())
    if c==1:
        inter=check(x)
        wood.pop(inter)
        wood_key.append(x)
        wood[inter[0]]=x
        wood[x]=inter[1]
    else:
        inter=check(x)
        ans=inter[1]-inter[0]
        print(ans)