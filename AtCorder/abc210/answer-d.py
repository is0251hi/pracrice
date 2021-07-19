h,w,c=map(int,input().split())
for _ in range(h):
    a=list(map(int,input().split()))
sum_value=[[0]*(w+1) for _ in range(h+1)]

for i in range(h):
    for j in range(w):
        sum_value[i+1][j+1]=a[i+1][j+1]+a[i][j]

