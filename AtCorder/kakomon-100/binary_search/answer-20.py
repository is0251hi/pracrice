#上段一つずつ調べる
#全組み合わせを調べるのは計算量的に無理(10**5)**3
#ソートして二分探索、近い値を見つけてそれ以下の数を調べる＊要素
#さらに下の段の要素で同様に二分探索して調べる*要素
def binary_search(num,n_list,n):
    cnt=1
    left=0
    right=n-1
    while left<right:
        mid=(left+right)//2
        if num<n_list[mid]:
            right=mid
        elif num>n_list[mid]:
            left=mid+1
        else:
            break
    idx=mid-1
    while idx>=0 and n_list[mid]==n_list[idx]:
        cnt+=1
        idx-=1
    idx=mid+1
    while idx<=n-1 and n_list[mid]==n_list[idx]:
        cnt+=1
        idx+=1
    return cnt

def main():
    ans=0
    n=int(input())
    a_l=list(map(int,input().split()))
    b_l=list(map(int,input().split()))
    c_l=list(map(int,input().split()))
    a_l.sort()
    c_l.sort()
    for b in b_l:
        a_cnt=0
        c_cnt=0
        a_cnt+=binary_search(b,a_l,n)
        c_cnt+=binary_search(b,c_l,n)
        ans+=(a_cnt*c_cnt)
    print(ans)
        
if __name__=='__main__':
    main()