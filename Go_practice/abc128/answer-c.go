package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)
var sc *bufio.Scanner
func nextInt() int{
	sc.Scan()
	i,e:=strconv.Atoi(sc.Text())
	if e!=nil{
		panic(e)
	}
	return i
}
type light struct{
	ss int
	p int
}
func main() {
	sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	n,m:=nextInt(), nextInt()
	lights:=make([]light int)
	for i := range lights {
        k := nextInt()
        for j := 0; j < k; j++ {
            s := nextInt()
            lights[i].ss += 1 << uint(s-1)
        }
    }
    for i := range lights {
        lights[i].p = nextInt()
    }
    ans := 0
    for x := 0; x < int(math.Pow(2.0, float64(n))); x++ {
        flg := true
        for _, l := range lights {
            elec := l.ss & x
            cnt := 0
            for i := 0; i < n; i++ {
                cnt += (elec >> uint(i)) & 1
            }
            if cnt%2 != l.p {
                flg = false
            }
        }
        if flg {
            ans++
        }
    }
    fmt.Println(ans)
}
