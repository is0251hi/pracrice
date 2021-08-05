def check(a,b):
    boolean=False
    if a<w-1 and b<h-1 :
        if c[a][b]==1 and seen[a][b]==0:
            boolean=True
    return boolean
def dfs():
    while stack:
        i,j=stack[-1]
        if check(i+1,j):
            i+=1
            seen[i][j]=1
            stack.append((i,j))
        elif check(i,j+1):
            j+=1
            seen[i][j]=1
            stack.append((i,j))
        elif check(i+1,j+1):
            i+=1
            j+=1
            seen[i][j]=1
            stack.append((i,j))
        else:
            stack.pop(-1)
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
                dfs()
                cnt+=1
    print(cnt)