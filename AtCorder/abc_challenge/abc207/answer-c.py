N = int(input())
n_list=[]
answer=0
for i in range(N):
    t,l,r= map(int,input().split())
    if t%2==0:
        r-=0.1
    if t>=3:
        l+=0.1
    n_list.append([l,r])
for i in range(N):
    for j in range(i+1,N):
        answer += (max(n_list[i][0],n_list[j][0]) <= min(n_list[i][1],n_list[j][1]))
print(answer)