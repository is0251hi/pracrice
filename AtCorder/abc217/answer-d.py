import sys
from collections import deque
sys.setrecursionlimit(10**6)
l,q=map(int,sys.stdin.readline().split())
wood=[(0,l)]
def check(num):
    for idx,w in enumerate(wood[::-1]):
        if w[0]<num<w[1]:
            inter=idx
            break
    return inter
for _ in range(q):
    c,x=map(int,sys.stdin.readline().split())
    if c==1:
        inter=check(x)
        w=wood[inter]
        wood[inter]=(0,0)
        wood.append((w[0],x))
        wood.append((x,w[1]))
    else:
        inter=check(x)
        ans=wood[inter][1]-wood[inter][0]
        print(ans)
