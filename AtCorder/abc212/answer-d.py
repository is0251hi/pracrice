def main():
    q=int(input())
    ans=0
    x_dict={}
    for _ in range(q):
        p,*x_l=map(int,input().split())
        if p==1:
            x=x_l[0]
            if x in x_dict:
                x_dict[x]+=1
            else:
                x_dict[x]=1
        elif p==2:
            x=x_l[0]
            temp={}
            for key,value in x_dict.items():
                temp[key+x]=value
            x_dict=temp
            del temp
        else:
            ans=min(x_dict)
            if x_dict[ans]==1:
                del x_dict[ans]
            else:
                x_dict[ans]-=1
            print(ans)
if __name__=='__main__':
    main()
