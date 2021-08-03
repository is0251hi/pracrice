def calc(x,p):
    return (x+p/(2**(x/1.5)))
def main():
    p=(input())
    left=0
    right=p-1
    ans=0
    while left<right:
        mid=right//2
        temp=calc(mid,p)
        if ans==0:
            ans=temp
        elif temp<=ans:
            left=mid+1
            ans=temp
        elif temp>ans:
            right=mid
    print(ans)
if __name__=='__main__':
    main()