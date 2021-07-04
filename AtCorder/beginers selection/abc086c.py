N = int(input())
t_list = []
dest = []
pos = [0,0]
check = True
before=0
for n in range(N):
    t,x,y = map(int,input().split())
    t_list.append(t)
    dest.append([x,y])

for idx,after in enumerate(t_list):
    time = after-before
    before = after
    diff = abs(dest[idx][0]-pos[0])+abs(dest[idx][1]-pos[1])
    if (diff <= time) and (time%2==diff%2):
        pos = dest[idx]
    else:
        check = False
        break
if check:
    print('Yes')
else:
    print('No')