s_l=['ABC','ARC','AGC','AHC']
s=[]
for _ in range(3):
    s.append(input())
ans=list(set(s_l)-set(s))
print(ans[0])