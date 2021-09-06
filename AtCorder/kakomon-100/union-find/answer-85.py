n,q=map(int,input().split())
class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents=[-1]*n
    def find(self,x):#親返す
        if self.parents[x]<0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return
        self.parents[x]+=self.parents[y]
        self.parents[y]=x
    def same(self,x,y):
        if self.find(x)==self.find(y):
            return 1
        else:
            return 0 
uf=UnionFind(n=n)
for _ in range(q):
    com,x,y=map(int,input().split())
    if com==1:
        print(uf.same(x,y))
    else:
        uf.union(x,y)
        