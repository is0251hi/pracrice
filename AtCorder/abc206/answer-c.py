import sys
N=int(sys.stdin.readline())
a_list = list(map(int,sys.stdin.readline().split()))
count=0

def bin_search(num,data):
    left=0
    right=len(data)
    boolean=False
    while left<right:
        mid = (left + right) // 2
        if data[mid] == num:
            boolean=True
            break
        elif data[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    if boolean==True:
        ex_count=0
        for idx in range(right-left):
            if num==data[left+idx]:
                ex_count+=1
        count=len(data)-ex_count
    else:
        count=len(data)
    print(count)
    return count
for idx,a in enumerate(a_list[:-2]):
    sorted_list=sorted(a_list[idx+1:])
    count+=bin_search(a,sorted_list)

print(count)
