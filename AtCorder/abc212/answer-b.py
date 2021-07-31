num_str=input()
num_list=[]
for num in num_str:
    num_list.append(int(num))
check=False
if num_list[0]*4==sum(num_list):
    check=True
else:
    cnt=0
    for i in range(3):
        if num_list[i]==9:
            if num_list[i+1]==0:
                cnt+=1
        else:
            if num_list[i]+1==num_list[i+1]:
                cnt+=1
    if cnt==3:
        check=True
if check:
    print('Weak')
else:
    print('Strong')