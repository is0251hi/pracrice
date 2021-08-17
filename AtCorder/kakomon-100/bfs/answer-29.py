import sys
from collections import deque
r,c=map(int,sys.stdin.readline().split())
sy,sx=map(int,sys.stdin.readline().split())
gy,gx=map(int,sys.stdin.readline().split())
road=[]
seen=[[0]*(c+1) for _ in range(r+1)]
check_l=[(-1,0),(0,-1),(1,0),(0,1)]
cnt=[[0]*(c+1) for _ in range(r+1)]
queue=deque()
for _ in range(r):
    pixels=sys.stdin.readline()
    b_l=[]
    for pixel in pixels: 
        if pixel=='#':
            b_l.append(1)
        else:
            b_l.append(0)
    road.append(b_l)

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
            if 0<=check_y and check_y<r and 0<=check_x and check_x<c and seen[check_y][check_x]==0 and road[check_y-1][check_x-1]==0:
                seen[check_y][check_x]=1
                cnt[check_y][check_x]=cnt[y][x]+1
                queue.append((check_x,check_y))
bfs()
print(cnt[gy][gx])

