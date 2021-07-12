while(True): # 入力数が決まってないため無限ループを作る
    n, x = map(int, input().split())
    if(n==0): break 
    res = 0 
    for a in range(1, n-1): # 全ての組み合わせを調べるループ、重複と入れ替えを除くやつ
        for b in range(a+1, n):
            c=x-a-b
            if c==a or c==b or (c<1 and c>n):
                continue
            if(a+b+c == x): 
                res += 1 # 条件を満たす時結果をインクリメント。 ++res としないように

    print(res)
