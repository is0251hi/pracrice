n=int(input())
st_dict={}
check=False
for _ in range(n):
    s,t=input().split()
    st=(s,t)
    if st in st_dict:
        check=True
        break
    st_dict[st]=1
if check:
    print('Yes')
else:
    print('No')