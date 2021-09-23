class Union_find:
    def __init__(self,n):
        self.parents=[-1]*n
    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    def union(self,a,b):
        x=self.find(a)
        y=self.find(b)
        if x==y:
            return
        if x>y:
            x,y=y,x
        self.parents[x]+=self.parents[y]
        self.parents[y]=x
    def group_cnt(self):
        cnt=[i for i,x in enumerate(self.parents) if x<0]
        return len(cnt)

n,m=map(int,input().split())
bridges=[]
ans=0
for _ in range(m):
    a,b=map(int,input().split())
    bridges.append((a-1,b-1))
for i in range(m):
    uf=Union_find(n)
    for j in range(m):
        if i==j:
            continue
        a,b=bridges[j]
        uf.union(a,b)
    if uf.group_cnt()!=1:
        ans+=1
print(ans)