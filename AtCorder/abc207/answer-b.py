import sys
blue,b,c,d= map(int,sys.stdin.readline().split())
red=0
if b>c:
    num=-1
else:
    num=0
    while 1:
        if blue<=(red*d):
            break
        num+=1
        blue+=b
        red+=c
print(num)