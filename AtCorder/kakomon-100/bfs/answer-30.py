from collections import deque
h,w,n=map(int,input().split())
town=[]
seen=[[0]*(w+1) for _ in range(h+1)]
queue=deque()
move_l=[(-1,0),(0,-1),(1,0),(0,1)]
for i in range(h):
    row=input()
    t=[]
    for j,r in enumerate(row):
        if type(r)==int:
            t.append(int(r))
        elif r=='.':
            t.append(0)
        else:
            if r=='S':start=(i,j)
            t.append(r)
        town.append(t)
        
def bfs():
    heart=1
    time=1
    queue.append(start)
    seen[start[1]][start[0]]=1
    while queue:
        x,y=queue.popleft()
        for move in move_l:
            d_x=move[0]+x
            d_y=move[1]+y
            if 0<=d_x<w and 0<=d_y<h and seen[d_y][d_x]==0:
                if type(town[d_y][d_x])==str and town[d_y][d_x]=='X':
                    continue
                elif type(town[d_y][d_x])==int and town[d_y][d_x]>heart:
                    continue
                if town[d_y][d_x]==0:heart+=1
                time+=1
                queue.append((d_x,d_y))
                seen[d_y][d_x]==1
    return time
time=bfs()
print(time)