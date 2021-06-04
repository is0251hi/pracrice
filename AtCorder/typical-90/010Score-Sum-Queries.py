import sys
n = int(sys.stdin.readline())
sum_value=[[0]*(n+1) for _ in range(2)]
for i in range(n):
    idx,value = map(int,sys.stdin.readline().split())
    sum_value[idx-1][i+1] = value

for i in range(n):
    for idx in range(2):
        sum_value[idx][i+1] += sum_value[idx][i]
q = int(sys.stdin.readline())
for i in range(q):
    answer_list=[]
    start,end = map(int,sys.stdin.readline().split())
    for idx in range(2):
        answer=sum_value[idx][end] - sum_value[idx][start-1]
        answer_list.append(answer)
    print(' '.join(map(str,answer_list)))