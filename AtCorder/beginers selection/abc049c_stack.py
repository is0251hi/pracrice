import sys
sys.setrecursionlimit(1000000)
N = sys.stdin.readline().replace('\n','')
string_list = ["dream","dreamer", "erase", "eraser"]
max_cnt=len(N)
check=False
stack=[0]
while stack:
    num=stack.pop()
    if max_cnt==num:
        check=True
        break
    temp=num
    for s in string_list:
        num=temp
        if num+len(s)>max_cnt:
            continue
        if s in N[num:num+len(s)]:
            num+=len(s)
            stack.append(num)
if check:
    print("YES")
else:
    print("NO")