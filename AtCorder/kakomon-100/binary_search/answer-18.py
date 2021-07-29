def binary_search(s,num):
    check=False
    left=0
    right=len(s)
    while left<right:
        idx=(left+right)//2
        if num==s[idx]:
            check=True
            break
        elif num>s[idx]:
            left=idx+1
        else:
            right=idx
    return check

def main():
    ans=0
    _=int(input())
    s=list(map(int,input().split()))
    q=int(input())
    t=list(map(int,input().split()))
    s.sort()
    for i in range(q):
        check=binary_search(s,t[i])
        if check:
            ans+=1
    print(ans)

if __name__=='__main__':
    main()