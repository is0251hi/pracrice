import math
w,h=map(int,input().split())
num=1000000007
w-=1
h-=1
ans=math.factorial(w+h)/(math.factorial(h)*math.factorial(w))
print(int(ans%num))