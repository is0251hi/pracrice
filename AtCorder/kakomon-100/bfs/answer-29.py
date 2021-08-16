import sys
from collections import deque
r,c=map(int,sys.stdin.readline().split())
sy,sx=map(int,sys.stdin.readline().split())
gy,gx=map(int,sys.stdin.readline().split())
road=[]
seen=[[0]*c for _ in range(r)]
check_l=[(-1,0),(0,-1),(1,0),(0,1)]
cnt=[[0]*c for _ in range(r)]
queue=deque()
for _ in range(r):
    c=sys.stdin.readline().split()
    c_l=[0 if a=='.' else 1 for a in c]
    road.append(c_l)

def bfs():
    seen[sy][sx]=1
    cnt[sy][sx]=0
    queue.append((sx,sy))
    while queue:
        x,y=queue.popleft()
        if x==gx and y==gy:
            break
        for check in check_l:
            check_y=check[1]+y
            check_x=check[0]+x
            if seen[check_y][check_x]==0 and road[check_y][check_x]==0:
                seen[check_y][check_x]=1
                cnt[check_y][check_x]=cnt[y][x]+1
                queue.append((check_x,check_y))
print(cnt[gy][gx])

