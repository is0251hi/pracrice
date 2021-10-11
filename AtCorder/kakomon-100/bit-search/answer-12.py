from itertools import combinations
N, M = map(int, input().split())
link = [[0 for i in range(N)] for j in range(N)]
for m in range(M):
    x, y = map(int, input().split())
    link[x-1][y-1] = 1
    link[y-1][x-1] = 1

for i in range(N,1,-1): # N, N-1, N-2, ... 2
    for comb in combinations(range(N),i):
        for c in combinations(comb, 2): # 議員の集合に対して考えられるペアを列挙
            if (link[c[0]][c[1]] == 0): # 一つでも知り合いでない組があればNG
                break
        else: # 派閥が作れた段階でプログラムを終了
            print (i)
            exit()
print (1)