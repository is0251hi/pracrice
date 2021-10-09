def check(x,y):
    if x==y:
        return 2
    elif x=='G':
        if y=='C':return 0
        else:return 1
    elif x=='C':
        if y=='P':return 0
        else:return 1
    elif x=='P':
        if y=='G':return 0
        else:return 1

n,m=map(int,input().split())
a_l=[]
for _ in range(2*n):
    a_str=input()
    l=[a for a in a_str]
    a_l.append(l)

rank=[[i,0]for i in range(2*n)]
for i in range(m):
    new_rank=[]
    for j in range(n):
        x=rank[2*j]
        y=rank[2*j+1]
        ch=check(a_l[x[0]][i],a_l[y[0]][i])
        if ch==0:
            x[1]+=1
        elif ch==1:
            y[1]+=1
        new_rank.append(x)
        new_rank.append(y)
    rank=sorted(new_rank,key=lambda x:(-x[1],x[0]))
for r in rank:
    print(r[0]+1)