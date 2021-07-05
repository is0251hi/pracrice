N = int(input())
num_list=[1]
answer=0
for n in range(2,11):
    num=n*num_list[n-2]
    if num >= N:
        break
    num_list.append(num)
for num in reversed(num_list):
    cnt=1
    check=True
    while check:
        if num*cnt > N:
            cnt-=1
            N-=num*cnt
            check=False
        else:
            cnt+=1
    answer+=cnt
print(answer)