n=int(input())
as=[]
bs=[]
for i in range(n):
    a,b=map(int,input().split())
    as.append(a)
    bs.append(b)
as.sort()
bs.sort()
x=as[n//2]
y=bs[n//2]
ans=0
for i in range(n):
    ans+=abs(as[i]-x)+abs(as[i]-bs[i])+abs(bs[i]-y)
print(ans)