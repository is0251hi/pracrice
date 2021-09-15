from collections import deque
n=int(input())
process=deque()
ball=n
while ball!=0:
    if ball%2==0:
        process.appendleft('B')
        ball//=2
    else:
        process.appendleft('A')
        ball-=1
ans=''.join(list(process))
print(ans)