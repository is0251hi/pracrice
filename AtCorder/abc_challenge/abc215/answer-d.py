#素数かつA_list内の数値を除く、除いた値の倍数も除く
n,m=map(int,input().split())
a_l=list(map(int,input().split()))
limit_num=max(max(a_l),m)
k=[True]*(limit_num+1)#条件を満たす数値のリスト
prime_l=[]#Aの素数で使えない
is_prime=[True]*(limit_num+1)
is_prime[0]=False
is_prime[1]=False
#同じ数であるか
for a in a_l:
    k[a]=False
#素因数であるか
def prime(limit):
    for i in range(2,int(limit**0.5)+1):
        if not is_prime[i]:
            continue
        for j in range(i*2,limit+1,i):
            is_prime[j]=False#iはjの素因数
            k[i]=k[i] and k[j]#jがAの要素ならiは使えない素数
        if not k[i]:
            prime_l.append(i)
prime(limit_num)
#倍数であるか
for p in prime_l:
    for p_multi in range(p*2,limit_num,p):
        k[p_multi]=k[p] and k[p_multi]
# 使える数をansに入れる
ans = [1]
for i in range(2,m+1):
    if k[i]:
        ans.append(i)
# 出力
print(len(ans))
for i in ans:
    print(i)

