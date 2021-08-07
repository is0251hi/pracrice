import sys
n,q=map(int,sys.stdin.readline().split())
part={}
ans=[0 for _ in range(n)]
for _ in range(n):
    a,b=map(int,sys.stdin.readline().split())
    if a in part:
        part[a].append(b)
    else:
        part[a]=[b]
def dfs_add(num):
    while stack:
        idx=stack.pop()
        for i in range(len(part[idx])):
            if seen[part[idx][i]-1]==0:
                ans[part[idx][i]-1]+=num
                if part[idx][i] in part:
                    stack.append(part[idx][i])
for _ in range(q):
    stack=[]
    seen=[0 for _ in range(n)]
    p,num=map(int,sys.stdin.readline().split())
    stack.append(p)
    dfs_add(num)
print(' '.join(ans))
