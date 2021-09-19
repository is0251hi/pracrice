x=input()
n=int(input())
s_l=[]
for _ in range(n):
    s_l.append(input())
x_d={}
for idx,a in enumerate(x):
    x_d[a]=idx+1
s_num={}
for s in s_l:
    num=''
    for a in s:
        if x_d[a]<10:num=num+'0'+str(x_d[a])
        else:num=num+str(x_d[a])
    if len(s)<10:
        num=num+('00'*(10-len(s)))
    s_num[s]=int(num)
ans_l=sorted(s_num.items(),key=lambda x:x[1])
for ans in ans_l:
    print(ans[0])

###別解####
#指定された文字列を数字ではなくabcに対応させる辞書を作る方法もある
#for i in range(26):
#    nxt = chr(i + ord('a'))  # 英小文字の前から数えてi番目（aを0番目とする）ord()でユニコードにして加算
#    D[X[i]] = nxt
#for char in s_l:
#    T += D[char]