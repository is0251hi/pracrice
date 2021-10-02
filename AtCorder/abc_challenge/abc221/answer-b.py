import copy
s=list(input())
t=list(input())
if s==t:
    print('Yes')
    exit()
else:
    for i in range(len(s)-1):
        word=copy.copy(s)
        a=word[i]
        b=word[i+1]
        word[i]=b
        word[i+1]=a
        if word==t:
            print('Yes')
            exit()
print('No')
