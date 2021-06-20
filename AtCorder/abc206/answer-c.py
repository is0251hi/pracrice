import sys
N=int(sys.stdin.readline())
a_list = list(map(int,sys.stdin.readline().split()))
answer = (N*N-N)/2
a_list.sort()
count=1
for idx,a in enumerate(a_list[1:]):
    if a!=a_list[idx]:
        answer -= (count*count-count)/2
        count=1
    else:
        count+=1
answer -= (count*count-count)/2
print(int(answer))

