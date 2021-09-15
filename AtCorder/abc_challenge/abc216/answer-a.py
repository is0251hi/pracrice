x,y=map(int,input().split('.'))
if y<=2:
    y_str='-'
elif y>=7:
    y_str='+'
else:
    y_str=''
print(str(x)+y_str)