import sys
sys.setrecursionlimit(10 ** 6)  # 再帰上限の引き上げ
# エラトステネスの篩。
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):#小さい素数の倍数の素数判定falseに
            is_prime[j] = False
    return is_prime # 要素が入ってるか確認するには、素の配列返しちゃったほうが楽

# 制約条件以下の素数を一通り取得する
LIMIT = 10**5+10
PRIME = primes(LIMIT)
# 2017に似てる数か？のフラグ。似てれば1
IS_LIKE = [0] * LIMIT
# IS_LIKEの一次元累積和を高速で求める用の配列
S = [0] * LIMIT

# 2017に似た数を制約条件まで一通り判定して、結果を配列に保存
for i in range(1,LIMIT,2):
    if PRIME[i] and PRIME[(i+1)//2]:
        IS_LIKE[i] = 1

# 一次元累積和用の前処理
for i in range(1,LIMIT):
    S[i] = S[i-1] + IS_LIKE[i]

Q = int(sys.stdin.readline())
for _ in range(Q):
    L, R = map(int, sys.stdin.readline().split())
    print(S[R] - S[L-1])