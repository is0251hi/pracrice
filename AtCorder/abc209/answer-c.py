n=int(input())
c_list=list(map(int,input().split()))
c_list.sort()
err=False
temp=0
cnt=1
answer=1
for idx,c in enumerate(c_list):
    if c==temp:
        cnt+=1
    else:
        if c<cnt:
            err=True
            break
        temp=c
        cnt=1
    answer*=(c-idx)
if err==False:
    print(answer%(10**9+7))
else:
    print(0)