import sys
a,b,c = map(int,sys.stdin.readline().split())
num = [a,b,c]
num.sort()
if num[0]==num[1]:
    print(num[2])
elif num[1]==num[2]:
    print(num[0])
else:
    print(0)
