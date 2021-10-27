package main

import "fmt"

//コメント

func main() {
	var N int
	ans := 0
	fmt.Scan(&N)
	for i := 1; i <= N; i += 2 {
		cnt := 0
		for j := 1; j <= i; j += 1 {
			if i%j == 0 {
				cnt += 1
			}
		}
		if cnt == 8 {
			ans += 1
		}
	}
	fmt.Println(ans)
}
