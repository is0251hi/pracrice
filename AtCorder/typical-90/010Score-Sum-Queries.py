import sys
n = int(sys.stdin.readline())
sum_value=[]
idx_list = []
for _ in range(n):
    idx,value = map(int,sys.stdin.readline().split())
    idx_list.append(idx)
    sum_value.append(value)

q = int(sys.stdin.readline())
for _ in range(q):
    start,end = map(int,sys.stdin.readline().split())
    num=start-1
    answer=[0,0]
    while num < end:
        if idx_list[num]==1:
            answer[0]+=sum_value[num]
        elif idx_list[num]==2:
            answer[1]+=sum_value[num]
        num+=1
    print(' '.join(map(str,answer)))