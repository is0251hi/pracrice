import sys
n = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
boolean=False
count=0
while boolean==False:
    for num in num_list:
        if num%2==1:
            boolean=True
            break
    if boolean==False:
        count+=1
    num_list=[num/2 for num in num_list]
print(count)