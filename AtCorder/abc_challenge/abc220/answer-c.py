n=int(input())
a_l=list(map(int,input().split()))
x=int(input())
a_sum=sum(a_l)
rot=x//a_sum
remain=x-(rot*a_sum)
for i,a in enumerate(a_l):
    remain-=a
    if remain<0:
        print(len(a_l)*rot+i+1)
        exit()