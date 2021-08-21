from math import factorial
s,k=input().split()
k=int(k)
all_l=set()
all_d={}
partern=1
for a in s:
    if a in all_d:
        all_d[a]+=1
    else:
        all_d[a]=1
    all_l.append(a)
all_l.sort()
print(all_l)
