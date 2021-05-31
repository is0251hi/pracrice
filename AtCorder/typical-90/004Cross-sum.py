import sys
row,column = map(int,sys.stdin.readline().split())
input_list = []
row_sum_list = []
column_sum_list = []

for r in range(row):
    temp=list(map(int,sys.stdin.readline().split()))
    input_list.append(temp)
    row_sum = sum(temp)
    row_sum_list.append(row_sum)

for c in range(column):
    column_sum = 0
    for r in range(row):
        column_sum += input_list[r][c]
    column_sum_list.append(column_sum)

for r in range(row):
    answer_row_list = []
    for c in range(column):
        answer_row_list.append(str(row_sum_list[r] + column_sum_list[c] - input_list[r][c]))
    print(' '.join(answer_row_list))