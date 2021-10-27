package samplepl

import "fmt"

type Car struct {
	tire  string
	speed int
}
type Handle interface {
	run()
	stop()
}

func run(c Car) {
	fmt.Println(c.speed)
}
func dash(c Car) {
	fmt.Println(c.speed * 2)
}

//メソッド、Car構造体に紐ずく関数
func CarFactory(t string, s int) Car {
	var c Car
	c.tire = t
	c.speed = s
	return c
}
