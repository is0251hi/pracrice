n=int(input())
s_l=list(map(int,input().split()))
t_l=list(map(int,input().split()))
time=0
#1周してくるパターン忘れていた
for i in range(n):
    if i>0:
        time=min(time+s_l[i-1],t_l[i])
        print(time)
    else:
        time=t_l[0]
        print(time)