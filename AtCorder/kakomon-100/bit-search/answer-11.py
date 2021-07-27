n,m=map(int,input().split())
s_list=[]
k_list=[]
for i in range(m):
    s=tuple(map(int,input().split()))
    k_list.append(s[0])
    s_list.append(s[1:])
p_list=tuple(map(int,input().split()))

#スイッチのON/OFF
on = [[False] * n for _ in range(1 << n)]
for bit in range(1<<n):
    for i in range(n):
        if bit & (1 << i):
            on[bit][i] = True
ans=0
for bit in range(1<<n):
    ok=True
    for i in range(m):
        total=0
        for j in range(k_list[i]):
            if on[bit][s_list[i][j]-1]:
                total+=1
        if not total%2==p_list[i]:
            ok=False
            break
    if ok:
        ans+=1
print(ans)
    
