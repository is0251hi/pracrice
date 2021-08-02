#上段一つずつ調べる
#全組み合わせを調べるのは計算量的に無理(10**5)**3
#ソートして二分探索、近い値を見つけてそれ以下の数を調べる＊要素
#bisectで二分探索、挿入するidxを探せる(すでにあれば左か右端を選べる)
import bisect
def main():
    ans=0
    n=int(input())
    a_l=list(map(int,input().split()))
    b_l=list(map(int,input().split()))
    c_l=list(map(int,input().split()))
    a_l.sort()
    c_l.sort()
    for b in b_l:
        a_cnt=bisect.bisect_left(a_l,b)
        c_cnt=bisect.bisect_right(c_l,b)
        ans+=a_cnt*(n-c_cnt)
    print(ans)
        
if __name__=='__main__':
    main()