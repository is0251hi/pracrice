n=int(input())
d={}
for _ in range(n):
    x,y=map(int,input().split())
    if x not in d:
        d[x]=[]
    d[x].append(y)
e={}
for i in d.values:
    i.sort()
    for j in range(len(i)):
        for k in range(j+1, len(i)):
            e[(i[j],i[k])]=e.get((i[j],i[k]), 0)+1
ans=0
for i in e.values():
    ans+=i*(i-1)//2
print(ans)
