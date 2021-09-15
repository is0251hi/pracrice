import sys
n,k = map(int,sys.stdin.readline().split())
sum_money=k
friend_dict = {}
money_list = []
for num in range(n):
    a,b = map(int,sys.stdin.readline().split())
    if a in friend_dict:
        friend_dict[a] += b
    else:
        friend_dict[a] = b
money_list=sorted(friend_dict.items(),key=lambda x:x[0])

for money in money_list:
    if sum_money < money[0]:
        break
    sum_money += money[1]

print(sum_money)