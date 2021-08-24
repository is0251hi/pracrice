import sys
q=int(sys.stdin.readline())
def prime(n):
    f=3
    if n==2:return True
    if n%2==0:return False
    while f*f<=n:
        if n%f==0:
            return False
        else:
            f+=2
    return True
for i in range(q):
    l,r=map(int,sys.stdin.readline().split())
    ans=0
    for j in range(l,r+1,2):
        if prime(j) and prime((j+1)/2):
            ans+=1
    print(ans)