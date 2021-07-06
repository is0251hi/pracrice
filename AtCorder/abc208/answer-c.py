N,K = map(int,input().split())
x=0  
a_list=list(map(int,input().split()))
a_sorted=sorted(a_list)
num=K//N
mod=K%N
if mod!=0:
    x=a_sorted[mod-1]
for a in a_list:
    if a<=x:
        print(num+1)
    else:
        print(num)