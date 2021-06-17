import sys
from typing import NamedTuple
N,Y = map(int,sys.stdin.readline().split())
boolean=False
def calc(x,y):
    z=N-x-y
    return (10000*x)+(5000*y)+(1000*z)

for i in range(0,N+1):
    for j in range(0,N-i+1):
        if calc(i,j) == Y:
            boolean=True
            k=N-i-j
            break
    else:
        continue
    break
if boolean==False:
    print(-1,-1,-1)
else:
    print(i,j,k)