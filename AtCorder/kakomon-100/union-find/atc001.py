n,q=map(int,input().split())
class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents=[-1]*n
    def find(self,num):
        if self.parents[num]<0:
            return num
        else:
            self.parents[num]=self.find(self.parents[num])
            return self.parents[num]
    def union(self,x,y):
        p_x=self.find(x)
        p_y=self.find(y)
        if p_x==p_y:
            return
        if self.parents[p_x]<self.parents[p_y]:#高い方に繋ぐ
            p_x,p_y=p_y,p_x
        self.parents[p_x]+=self.parents[p_y]
        self.parents[p_y]=p_x
    def check(self,x,y):
        return self.find(x)==self.find(y)
uf=UnionFind(n)
for _ in range(q):
    p,a,b=map(int,input().split())
    if p==0:
        uf.union(a,b)
    else:
        if uf.check(a,b):
            print('Yes')
        else:
            print('No')
