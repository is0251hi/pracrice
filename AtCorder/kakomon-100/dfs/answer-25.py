def check(a,b):
    return 0<=a<h and 0<=b<w and c[a][b]==1 and seen[a][b]==0 and not a==b==0
def dfs():
    while stack:
        i,j=stack.pop()
        for x in range(-1,2):
            for y in range(-1,2):
                x_idx=i+x
                y_idx=j+y
                if check(x_idx,y_idx):
                    seen[x_idx][y_idx]=1
                    stack.append((x_idx,y_idx))
while 1:
    w,h=map(int,input().split())
    if w==h==0:
        break
    seen=[[0]*w for _ in range(h)]
    c=[]
    stack=[]
    cnt=0
    for _ in range(h):
        c.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if c[i][j]==1 and seen[i][j]==0:
                stack.append((i,j))
                seen[i][j]=1
                dfs()
                cnt+=1
    print(cnt)