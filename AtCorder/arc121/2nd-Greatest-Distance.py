import sys
num = int(sys.stdin.readline())
idx = 0
input_list = []
x_list = []
y_list = []
answer_list = []
for n in range(num):
    x,y = map(int,sys.stdin.readline().split())
    idx+=1
    input_list.append([x,y,idx])
x_list=sorted(input_list,key=lambda x:x[0])
y_list=sorted(input_list,key=lambda x:x[1])
for n in range(2):
    reverse_n = -1-n
    answer_list.append(x_list[reverse_n]-x_list[0])#
    answer_list.append(y_list[reverse_n]-y_list[0])#
    if n == 1 and num == 3:
        pass
    else:
        answer_list.append(x_list[reverse_n]-x_list[1])#
        answer_list.append(y_list[reverse_n]-y_list[1])#
answer_list.sort()#
answer=abs(answer_list[-2])#
print(answer)
