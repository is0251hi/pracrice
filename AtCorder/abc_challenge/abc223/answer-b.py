from collections import deque
s=input()
queue=deque()
for a in s:
    queue.append(a)
ans_max=s
ans_min=s
for i in range(len(s)): 
    first=queue.popleft()
    queue.append(first)
    ans_max=max(''.join(queue),ans_max)
    ans_min=min(''.join(queue),ans_min)
print(ans_min)
print(ans_max)