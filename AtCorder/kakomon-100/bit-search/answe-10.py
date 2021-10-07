n=int(input())
a_l=list(map(int,input().split()))
q=int(input())
m_l=list(map(int,input().split()))

for m in m_l:
    for bit in range(1<<n):
        ans=0
        for i in range(n):
            if bit&(1<<i):
                ans+=a_l[i]
        if m==ans:
            print('yes')
            break
    else:
        print('no')