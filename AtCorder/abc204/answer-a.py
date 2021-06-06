import sys
answer_list=[0,1,2]
x,y = map(int,sys.stdin.readline().split())

if x==y:
    print(x)
else:
    print(3-x-y)