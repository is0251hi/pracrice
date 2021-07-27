n,m=map(int,input().split())
s_list=[]
k_list=[]
for i in range(m):
    s=tuple(map(int,input().split()))
    k_list.append(s[0])
    s_list.append(s[1:])
p_list=tuple(map(int,input().split()))

#スイッチのON/OFF
on = [[0] * n for _ in range(1 << n)]
for bit in range(1<<n):
    for i in range(n):
        print(bit,(1 << i))
        print(bit & (1 << i))
        if bit & (1 << i):#2**nとnまでの数のAND積(2進数)
            on[bit][i]=1 
ans=0
#全探索(2**nのパターンに対して、電球それぞれが期待通りか)
for bit in range(1<<n):
    ok=True
    for i in range(m):
        total=0
        for j in range(k_list[i]):
            if on[bit][s_list[i][j]-1]==1:
                total+=1
        if not total%2==p_list[i]:
            ok=False
            break
    if ok:
        ans+=1
print(ans)
    
