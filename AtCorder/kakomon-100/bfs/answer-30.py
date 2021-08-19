from collections import deque
h,w,n=map(int,input().split())
ans=0
town=[]
move_l=[(-1,0),(0,-1),(1,0),(0,1)]
place={}
for i in range(h):
    row=input()
    t=[]
    for j,r in enumerate(row):
        if r=='X':
            t.append(r)
        elif r=='.':
            t.append(0)
        elif r=='S':
            place[0]=(j,i)
            t.append(0)
        else:
            place[int(r)]=(j,i)
            t.append(int(r))
    town.append(t)
def bfs(start,goal):
    queue=deque()
    queue.append(start)
    seen=[[0]*w for _ in range(h)]
    seen[start[1]][start[0]]=1
    dist=[[0]*w for _ in range(h)]
    while queue:
        x,y=queue.popleft()
        if goal==(x,y):
            break
        for move in move_l:
            d_x=move[0]+x
            d_y=move[1]+y
            if 0<=d_x<w and 0<=d_y<h and seen[d_y][d_x]==0 and type(town[d_y][d_x])==int:
                dist[d_y][d_x]=dist[y][x]+1
                queue.append((d_x,d_y))
                seen[d_y][d_x]=1
    return dist[goal[1]][goal[0]]
for i in range(n):
    ans+=bfs(place[i],place[i+1])
print(ans)