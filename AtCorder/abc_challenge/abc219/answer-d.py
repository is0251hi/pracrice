n=int(input())
x,y=map(int,input().split())
ben_l=[]
for _ in range(n):
    a,b=map(int,input().split())
    ben_l.append((a,b))
ben_a=sorted(ben_l,key=lambda x:x[0])
ben_b=sorted(ben_l,key=lambda x:x[0])
a_ch=0
b_ch=0
for ben in ben_l:
    a_ch+=ben[0]
    b_ch+=ben[1]
if a_ch<x or b_ch<y:
    print(-1)
    exit()
con_check=True
sum_a=0
sum_b=0
idx=0
while con_check:
    idx+=1
    if x>y:
        a,b=ben_a.pop(-1)
        sum_a+=a
        sum_b+=b
    else:
        a,b=ben_b.pop(-1)
        sum_a+=a
        sum_b+=b
    if sum_a>=x and sum_b>=y:
        con_check=False
print(idx)