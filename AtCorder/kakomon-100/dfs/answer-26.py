import sys
n,q=map(int,sys.stdin.readline().split())
part={}
ans=[0]*n
for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    if a in part:
        part[a].append(b)
    else:
        part[a]=[b]
def dfs_add(num):
    while stack:
        idx=stack[-1]
        if not idx in part:
            continue
        for i in range(len(part[idx])):
            if seen[part[idx][i]-1]==0:
                seen[part[idx][i]-1]=1
                ans[part[idx][i]-1]+=num
                stack.append(part[idx][i])
                break
        else:
            idx=stack.pop(-1)
for _ in range(q):
    stack=[]
    seen=[0]*n
    p,num=map(int,sys.stdin.readline().split())
    ans[p-1]+=num
    stack.append(p)
    seen[p-1]=1
    dfs_add(num)
print(' '.join(list(map(str,ans))))
