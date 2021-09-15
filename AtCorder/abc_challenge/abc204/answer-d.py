import numpy as np
 
N = 4
T = [10,1,1,1]
S = np.sum(T)
DP = np.zeros(S//2+1,dtype=np.bool)
DP[-1] = 1

for i in range(N):
    print(DP)
    print(S//2+1-T[i])
    if S//2+1-T[i] < 0: 
        continue
    print(DP[:S//2+1-T[i]])
    print(DP[T[i]:])
    DP[:S//2+1-T[i]] |= DP[T[i]:] #numpyを用いていっぺんに遷移
print(DP)
print(S-S//2+np.argmax(DP))