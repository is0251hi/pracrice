import sys
import math
n=int(sys.stdin.readline())
t=206
n*=1.08
ans=math.floor(n)
if ans==t:
    print('so-so')
elif ans<t:
    print('Yay!')
else:
    print(':(')