n,x=map(int,input().split())
a_list=list(map(int,input().split()))
diff=n//2
if x>=sum(a_list)-diff:
    print('Yes')
else:
    print('No')