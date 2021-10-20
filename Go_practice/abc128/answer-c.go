package main

import (
	"fmt"
)

func main() {
	var (
		N int
		M int
		K int
		S [][]int
	)
	fmt.Scan(&N, &M)
	S = make([][]int, M)
	for i := range S {
		fmt.Scan(&K)
		S[i] = make([]int, K)
		for j := 0; j < M; j++ {
			fmt.Scan(&S[i][j])
		}

	}
}
