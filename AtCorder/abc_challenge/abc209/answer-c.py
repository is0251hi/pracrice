n=int(input())
c_list=list(map(int,input().split()))
c_list.sort()
err=False
answer=1
for idx in range(n):
    c=c_list[idx]
    if c<idx:
        err=True
        break

    answer=answer*(c-idx)%(10**9+7)
if err==False:
    print(answer)
else:
    print(0)