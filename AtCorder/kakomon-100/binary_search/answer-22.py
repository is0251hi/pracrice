def calc(x,p):
    return x+p*2**(-x/1.5)
def is_high(i,j,p):
    return calc(i,p)>=calc(j,p)
def main():
    p=float(input())
    left=0
    right=p
    while right-left>1*(10**-9):
        mid_right=(right*2+left)/3
        mid_left=(right+left*2)/3
        if is_high(mid_right,mid_left,p):
            right=mid_right
        else:
            left=mid_left
    print(calc(mid_right,p))
if __name__=='__main__':
    main()