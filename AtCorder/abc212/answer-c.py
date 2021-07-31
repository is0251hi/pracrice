def binary_search(a,num_list,m):
    left=0
    right=m-1
    check=False
    if m==1:return abs(num_list[0]-a)
    while(left<right):
        mid=(left+right)//2  
        if a>num_list[mid]:
            left=mid+1
        elif a<num_list[mid]:
            right=mid
        else:
            check=True
            diff=0
            break
    if check:return diff
    if left==0:
        diff=min(abs(num_list[left]-a),abs(num_list[left+1]-a))
    elif left==m-1:
        diff=min(abs(num_list[left]-a),abs(num_list[left-1]-a))
    else:
        diff=min(abs(num_list[left-1]-a),abs(num_list[left]-a),abs(num_list[left+1]-a))
    return diff

def main():
    ans=0
    n,m=map(int,input().split())
    a_list=list(map(int,input().split()))
    b_list=list(map(int,input().split()))
    b_list.sort()
    for i in range(n):
        diff=binary_search(a_list[i],b_list,m)
        if i==0:ans=diff
        else:
            ans=min(ans,diff)
            if ans==0:break
    print(ans)

if __name__=='__main__':
    main()
