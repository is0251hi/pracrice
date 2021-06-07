import sys
sys.setrecursionlimit(10000)
n,m= map(int,sys.stdin.readline().split())
load_dict={idx:[] for idx in range(n)}
for num in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if load_dict.get(a-1):
        load_dict[a-1].append(b-1)
    else:
        load_dict[a-1]=[b-1]
def dfs(v):
    if temp[v]: 
        return
    temp[v]=True
    for load in load_dict[v]:
        dfs(load)
answer=0
for idx in range(n):
    temp=[False]*(n)
    dfs(idx)
    answer+=sum(temp)
print(answer)