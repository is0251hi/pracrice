import sys
n,k = map(int,sys.stdin.readline().split())
std = (k*k//2)+1
height_list=[]
for num in n:
    height = map(int,sys.stdin.readline().split())
    height_list.append(height)
