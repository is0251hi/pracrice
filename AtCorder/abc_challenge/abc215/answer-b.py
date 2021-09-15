n=int(input())
i=0
while 1:
    if n<2**i:
        break
    i+=1
print(i)