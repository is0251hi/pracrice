n=int(input())
if n<2:
    print(1)
    exit()
fib=[0]*(n+1)
fib[0]=1
fib[1]=1
for i in range(2,n+1):
    if i==2:fib_2=1
    fib_1=fib[i-1]
    fib[i]=fib_1+fib_2
    fib_2=fib_1
print(fib[n])

