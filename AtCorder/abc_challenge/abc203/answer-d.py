import sys
n,k = map(int,sys.stdin.readline().split())
std = (k*k//2)+1
row=[]
input_list=[]
sum_list = [[0] * (n + 1) for _ in range(n + 1)]

for num in range(n):
    row = list(map(int,sys.stdin.readline().split()))
    input_list.append(row)

def check(mid):
    for i in range(n):
        for j in range(n):
            sum_list[i+1][j+1] = sum_list[i+1][j] + sum_list[i][j+1] - sum_list[i][j]
            if input_list[i][j] > mid:
                sum_list[i+1][j+1]+=1
    for i in range(n-k+1):
        for j in range(n-k+1):
            if sum_list[i+k][j+k] - sum_list[i][j+k] - sum_list[i+k][j] + sum_list[i][j] < std:
                return True
    return False

ng = -1
ok = 10**9+1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
    