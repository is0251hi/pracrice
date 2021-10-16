package main

import (
	"fmt"
	"os"
)

func main() {
	var N int
	fmt.Scan(&N)
	var ans int
	first := 1
	second := 1
	if N <= 1 {
		fmt.Println(1)
		os.Exit(0)
	}
	for i := 2; i <= N; i++ {
		ans = first + second
		first = second
		second = ans
	}
	fmt.Println(ans)
}
