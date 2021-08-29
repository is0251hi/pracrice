import math
n=int(input())
def divisor_sum(num):
    n_l=[]
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0 and n!=i:
            n_l.append(i)
            if num/i!=i and num/i!=num:
                n_l.append(num/i)
    n_sum=sum(n_l)
    return n_sum
n_sum=divisor_sum(n)
if n_sum==n:
    print('Perfect')
elif n_sum<n:
    print('Deficient')
else:
    print('Abundant')