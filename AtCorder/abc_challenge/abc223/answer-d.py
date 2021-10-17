
n,m=map(int,input().split())
terms=[]
behind=[]
for _ in range(m):
    a,b=map(int,input().split())
    terms.append(a)
    behind.append(b)
num_list=[i for i in range(n)if i not in behind]
num_list.sort()
for num in num_list:
    if num in terms:
        