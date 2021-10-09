n=int(input())
if n>=1000:
    print(n)
elif 100<=n<1000:
    print('0'+str(n))
elif 10<=n<100:
    print('00'+str(n))
else:
    print('000'+str(n))
