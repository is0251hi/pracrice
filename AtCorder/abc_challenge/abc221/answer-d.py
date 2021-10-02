n=int(input())
points=[[]]*n
mode_l=[]*n#modeのsumをとる
for idx in range(n):
    a,b=map(int,input().split())
    if a>n:
        continue
    points[a-1].append(idx)
    points[a+b-1].append(idx)#endは入れない
for point in points:
    for p in point:
        if mode_l[p]==1:
            mode_l[p]=0
        else:
            mode_l[p]=1
    print(sum(mode_l))