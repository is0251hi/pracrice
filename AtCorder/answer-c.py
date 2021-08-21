from itertools import permutations
s,k=input().split()
k=int(k)
all_moji=[]
partern=1
for a in s:
    all_moji.append(a)
all_l=list(permutations(all_moji))
all_l.sort()
all_s=set(all_l)
ans=''
for i,moji_l in enumerate(all_s):
    if i==k-1:
        for moji in moji_l:
            ans+=moji
        break
print(ans)
