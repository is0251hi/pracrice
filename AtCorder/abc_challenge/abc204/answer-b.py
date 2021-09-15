import sys
n = int(sys.stdin.readline())
a_list = list(map(int,sys.stdin.readline().split()))
sum_a=0
for a in a_list:
    if a<=10:
        continue
    sum_a+=a-10
print(sum_a)