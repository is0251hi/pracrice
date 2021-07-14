n,m=map(int,input().split())
a_list=[]
max_num=0
for _ in range(n):
    a_list.append(list(map(int,input().split())))
for a in range(m-1):
    for b in range(a+1,m):
        target=0
        for c in range(n):
            target+=max(a_list[c][a],a_list[c][b])
        if max_num<target:
            max_num=target
print(max_num)