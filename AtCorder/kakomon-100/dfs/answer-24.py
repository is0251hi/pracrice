n=int(input())
u_list=[]
k_list=[]
v_list=[]
time=0
d=[0 for _ in range(0,n+1)]
f=[0 for _ in range(0,n+1)]
for _ in range(n):
    u,k,*v=map(int,input().split())
    u_list.append(u)
    k_list.append(k)
    v_list.append(v)
def dfs(time,stack):
    while stack:
        time+=1
        num=stack[-1]
        if len(v_list[num-1])==0:
            f[stack.pop()]=time
        else:
            temp=v_list[num-1].pop(0)
            stack.append(temp)
            if d[temp]==0:
                d[temp]=time
    return time
stack=[]
for i in range(0,n):
    num=u_list[i]
    if d[num]==0:
        time+=1
        d[num]=time
        stack.append(num)
        time=dfs(time,stack)
for i in range(1,n+1):
    print(u_list[i-1],d[i],f[i])