from collections import deque
n,k=map(int,input().split())
c_list=list(map(int,input().split()))
temp=deque()
for i in range(0,k):
    temp.append(c_list[i])
    max_num=len(set(temp))
for j in range(k,n):
    temp.append(c_list[j])
    temp.popleft()
    num=len(set(temp))
    if num>max_num:
        max_num=num
print(max_num)