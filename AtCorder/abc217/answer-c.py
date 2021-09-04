n=int(input())
p_l=map(int,input().split())
q_l=[0]*(n+1)
for idx,p in enumerate(p_l):
    q_l[p]=idx+1
print(' '.join(map(str,q_l[1:])))