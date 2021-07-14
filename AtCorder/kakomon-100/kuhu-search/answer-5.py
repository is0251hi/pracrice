a,b,c,x,y=map(int,input().split())
money=0
max_cnt=max(x,y)
min_cnt=min(x,y)
diff=max_cnt-min_cnt
money+=min(((a*min_cnt)+(b*min_cnt)),(2*c*min_cnt))
if x>y:
    money+=min(a*diff,(2*c*diff))
else:
    money+=min(b*diff,(2*c*diff))
print(money)