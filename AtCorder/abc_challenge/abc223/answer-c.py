N=int(input())
douka_l=[]
total_time=0
distance=0
for _ in range(N):
    a,b=map(int,input().split())
    total_time+=a/b
    douka_l.append((a,b))
half_time=total_time/2
time=0
for douka in douka_l:
    time+=douka[0]/douka[1]
    if time>half_time:break
    distance+=douka[0]
if time==half_time:
    print(distance)
else:
    distance+=douka[0]-(douka[1]*(time-half_time))
    print(distance)
