s_l=[]
for _ in range(3):
    s=input()
    s_l.append(s)
t=input()
for a in t:
    print(s_l[int(a)-1],end='')