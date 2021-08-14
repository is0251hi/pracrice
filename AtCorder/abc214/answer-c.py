n=int(input())
s_l=list(map(int,input().split()))
t_l=list(map(int,input().split()))
time=0
#1周してくるパターン忘れていた
time_l=[]
for i in range(n):
    if i>0:
        time=min(time+s_l[i-1],t_l[i])
        time_l.append(time)
    else:
        time=t_l[0]
        time_l.append(time)
ans=0
for i,time in enumerate(time_l):
    if i>0:
        ans=min(ans+s_l[i-1],time)
        print(ans)
    else:
        ans=min(time_l[-1]+s_l[-1],time)
        print(ans)