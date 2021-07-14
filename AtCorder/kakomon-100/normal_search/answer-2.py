n=int(input())
answer=0
for i in range(1,n+1,2):
    cnt=1
    if i>=15:
        max_num=i//3+1#偶数なしかつ約数なので最小1/3
        for j in range(1,max_num,2):
            if i%j==0:
                cnt+=1
        if cnt==8:
            answer+=1
print(answer)