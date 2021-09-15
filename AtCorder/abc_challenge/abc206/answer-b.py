import sys
N=int(sys.stdin.readline())
num=0
count=0
while num<N:
    count+=1
    num+=count
print(count)