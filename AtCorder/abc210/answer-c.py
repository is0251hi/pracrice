n,k=map(int,input().split())
c_list=list(map(int,input().split()))
temp={}
for i in range(0,k):
    if c_list[i] in temp:
        temp[c_list[i]]+=1
    else:
        temp[c_list[i]]=1
    max_num=len(temp)
for j in range(k,n):
    if c_list[j] in temp:
        temp[c_list[j]]+=1
    else:
        temp[c_list[j]]=1
    if c_list[j-k] in temp:#in list遅いらしい->set,dictにすると良い
        if temp[c_list[j-k]]==1:
            temp.pop(c_list[j-k])
        else:
            temp[c_list[j-k]]-=1
    num=len(temp)
    max_num=max(num,max_num)
print(max_num)