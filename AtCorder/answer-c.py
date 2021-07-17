from collections import deque
n,k=map(int,input().split())
c_list=list(map(int,input().split()))
temp={}
for i in range(0,k):
    if i in temp:
        temp[c_list[i]]+=1
    else:
        temp[c_list[i]]=1
    max_num=len(temp)
for j in range(k,n):
    if i in temp:
        temp[c_list[i]]+=1
    else:
        temp[c_list[i]]=1
    if temp[c_list[i-k]]==1:
        temp[c_list[i-k]].pop()
    else:
        temp[c_list[i-k]]-=1
    max_num=max(num,max_num)
print(max_num)