n,p=map(int,input().split())
a_l=list(map(int,input().split()))
ans=0
for a in a_l:
    if a<p:
        ans+=1
print(ans)