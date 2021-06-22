import sys
sys.setrecursionlimit(1000000)
N = sys.stdin.readline().replace('\n','')
string_list = ["dream","dreamer", "erase", "eraser"]
max_cnt=len(N)
def dfs(num):
    if max_cnt==num:
        return True
    for s in string_list:
        if num+len(s)>max_cnt:
            continue
        if s in N[num:num+len(s)]:
            num+=len(s)
            check=dfs(num)
            if check:
                break
            else:
                num-=len(s)
    else:
        return False
    return True
check=dfs(0)
if check:
    print("YES")
else:
    print("NO")