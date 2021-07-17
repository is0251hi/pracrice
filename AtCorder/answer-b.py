n=int(input())
s=input()
cnt=0
for i in s:
    cnt+=1
    if i=='1':
        break
if cnt%2==0:
    print('Aoki')
else:
    print('Takahashi')