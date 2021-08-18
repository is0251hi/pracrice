from collections import deque
h,w,n=map(int,input().split())
town=[]
seen=[[0]*w for _ in range(h)]
dist=[[0]*w for _ in range(h)]
queue=deque()
move_l=[(-1,0),(0,-1),(1,0),(0,1)]
for i in range(h):
    row=input()
    t=[]
    for j,r in enumerate(row):
        if r=='X':
            t.append(r)
        elif r=='.':
            t.append(0)
        elif r=='S':
            start=(i,j)
            t.append(0)
        else:
            t.append(int(r))
    town.append(t)
def bfs():
    ans=0
    heart=1
    queue.append(start)
    seen[start[1]][start[0]]=1
    while queue:
        x,y=queue.popleft()
        for move in move_l:
            d_x=move[0]+x
            d_y=move[1]+y
            if 0<=d_x<w and 0<=d_y<h and seen[d_y][d_x]==0 and type(town[d_y][d_x])==int and town[d_y][d_x]<=heart:
                dist[d_y][d_x]=dist[y][x]+1
                queue.append((d_x,d_y))
                seen[d_y][d_x]=1
                if town[d_y][d_x]>0:
                    heart+=1
                    ans=max(ans,dist[d_y][d_x])
    return ans
print(bfs())