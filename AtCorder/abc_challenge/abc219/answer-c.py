x=input()
n=int(input())
s_l=[]
for _ in range(n):
    s_l.append(input())
x_d={}
for idx,a in enumerate(x):
    x_d[a]=idx+1
s_num={}
for s in s_l:
    num=''
    for a in s:
        if x_d[a]<10:num=num+'0'+str(x_d[a])
        else:num=num+str(x_d[a])
    if len(s)<10:
        num=num+('00'*(10-len(s)))
    s_num[s]=int(num)
ans_l=sorted(s_num.items(),key=lambda x:x[1])
for ans in ans_l:
    print(ans[0])