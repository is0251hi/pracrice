from itertools import combinations
n=int(input())
ls=[]
for i in range(n):
    ls.append(tuple(map(int,input().split())))
st = set(ls)
ans = 0
for p1, p2 in combinations(ls, 2): # 組み合わせでOK
    x1, y1 = p1
    x2, y2 = p2
    if (x2 + y2 - y1, y2 + x1 - x2) in st and (x1 + y2 - y1, y1 + x1 - x2) in st:
        ans = max(ans, (x1-x2)**2+(y1-y2)**2)
print (ans)