import sys
n,m= map(int,sys.stdin.readline().split())
idx_list=[]
load_dict={}
for num in m:
    a,b = map(int,sys.stdin.readline().split())
    if load_dict.get(a):
        load_dict[a].append(b)
    else:
        load_dict[a]=[b]
        idx_list.append(a)
for idx in idx_list:
    load_dict[idx]=set(load_dict[idx])
    