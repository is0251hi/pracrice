n=int(input())
s_l=[]
t_l=[]
for _ in range(n):
    s=input()
    a_l=[a for a in s]
    s_l.append(a_l)
for _ in range(n):
    t=input()
    a_l=[a for a in t]
    t_l.append(a_l)
def rotate(t_l):
    new_l=[]
    for j in reversed(range(0,n)):
        new=[]
        for i in range(n):
            new.append(t_l[i][j])
        new_l.append(new)
    return new_l
def find_leftop(s):
    for i in range(n):
        for j in range(n):
            if s[i][j]=='#':
                return i,j
def check():
    si,sj=find_leftop(s_l)
    ti,tj=find_leftop(t_l)
    diff_i=ti-si
    diff_j=tj-sj
    for i in range(n):
        for j in range(n):
            ii=i+diff_i
            jj=j+diff_j
            if 0<=ii<n and 0<=jj<n:
                if s_l[i][j]!=t_l[ii][jj]: return False
            else:
                if s_l[i][j]=='#': return False
    return True
cntS = sum(1 for i in range(n) for j in range(n) if s_l[i][j]=='#')
cntT = sum(1 for i in range(n) for j in range(n) if t_l[i][j]=='#')
if cntS != cntT:
	print("No")
	exit()
for _ in range(4):
    boolean=check()
    if boolean:break
    t_l=rotate(t_l)
if boolean:
    print('Yes')
else:
    print('No')