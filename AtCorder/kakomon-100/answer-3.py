s=input()
word=['A','C','G','T']
cnt=0
answer=0
for a in s:
    for w in word:
        if a==w:
            cnt+=1
            break
    else:
        cnt=0
    if answer<cnt: 
        answer=cnt
print(answer)
