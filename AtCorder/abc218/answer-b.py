p_l=list(map(int,input().split()))
s='abcdefghijklmnopqrstuvwxyz'
s_l=[a for a in s]
for p in p_l:
    print(s_l[p-1],end='')