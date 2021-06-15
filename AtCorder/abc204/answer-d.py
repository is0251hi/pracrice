import numpy as np
 
N = int(input())
T = list(map(int, input().split()))
S = np.sum(T)
DP = np.zeros(S//2+1,dtype=np.bool)
DP[-1] = 1

for i in range(N):
    if S//2+1-T[i] < 0: 
        continue
    DP[:S//2+1-T[i]] |= DP[T[i]:] #numpyを用いていっぺんに遷移
print(S-S//2+np.argmax(DP))