w,h=map(int,input().split())
mod=1000000007
w-=1
h-=1
num=1
den=1
for i in range(w):
    num*=(w+h-i)
    num%=mod
    den*=(i+1)
    den%=mod
print(num*pow(den,-1,mod)%mod)
