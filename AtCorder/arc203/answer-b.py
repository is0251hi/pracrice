import sys
n,k = map(int,sys.stdin.readline().split())
sum_num = 0
for a in range(1,n+1):
    for b in range(1,k+1):
        sum_num+=(a*100)+b
print(sum_num)