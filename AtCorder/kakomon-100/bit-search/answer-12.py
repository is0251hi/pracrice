from itertools import combinations
N, M = map(int, input().split())
link = [[0]*(N+1) for i in range(N+1)]
for m in range(M):
    x, y = map(int, input().split())
    link[x][y] = 1
    link[y][x] = 1
ans=0
for bit in range(1<<N):
    group=[]
    for i in range(N):
        if bit & (1<<i):#一桁ずつチェックし、1であれば加える
            group.append(i+1)
    check=True
    for comb in combinations(group,2):
        if link[comb[0]][comb[1]]==0:
            check=False
            break
    if check:ans=max(ans,len(group))
print(ans)