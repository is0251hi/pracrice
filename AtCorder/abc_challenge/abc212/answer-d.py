import heapq
def main():
    q=int(input())
    cnt=0
    x_list=[]
    for _ in range(q):
        p=list(input().split())
        if p[0]=='1':
            heapq.heappush(x_list,int(p[1])-cnt)
        elif p[0]=='2':
            cnt+=int(p[1])
        else:
            print(heapq.heappop(x_list)+cnt)
if __name__=='__main__':
    main()
