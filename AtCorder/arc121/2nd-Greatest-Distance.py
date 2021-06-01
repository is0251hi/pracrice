import sys
num = int(sys.stdin.readline())
x_list = []
y_list = []
answer_list = []
for _ in range(num):
    x,y = map(int,sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)
max_x = max(x_list)
max_y = max(y_list)
min_x = min(x_list)
min_y = min(y_list)

answer_list=[max(max_x-x,x-min_x,max_y-y,y-min_y)for x,y in zip(x_list,y_list)]
answer_list.sort()
print(answer_list[-3])