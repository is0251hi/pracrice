n=int(input())
a_s=[]
b_s=[]
for i in range(n):
    a,b=map(int,input().split())
    a_s.append(a)
    b_s.append(b)
a_s.sort()
b_s.sort()
x=a_s[n//2]
y=b_s[n//2]
ans=0
for i in range(n):
    ans+=abs(a_s[i]-x)+abs(a_s[i]-b_s[i])+abs(b_s[i]-y)
print(ans)