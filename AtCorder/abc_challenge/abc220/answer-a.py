a,b,c=map(int,input().split())
x=c
idx=1
while x<=b:
    if a<=x<=b:
        print(x)
        exit()
    idx+=1
    x*=idx
print(-1)