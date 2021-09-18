n=int(input())
if n>=90:
    print('expert')
elif 70<=n<90:
    print(90-n)
elif 40<=n<70:
    print(70-n)
else:
    print(40-n)