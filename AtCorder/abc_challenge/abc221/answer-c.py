n=list(input())
ans=0
n.sort()
for i in range(1<<len(n)):#全パターン
    l=0
    r=0
    for j in range(len(n)):#1パターンの全桁
        if i & (1<<j):
            l=l*10+ord(n[j])-ord('0')
        else:
            r=r*10+ord(n[j])-ord('0')
    ans=max(ans,l*r)
print(ans)