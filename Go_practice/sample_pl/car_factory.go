package samplepl

import "fmt"

type Car struct {
	tire  string
	speed int
}
type Handle interface {
	Run()
	Dash()
}

//メソッド、Car構造体に紐ずく関数
func (c Car) Run() {
	fmt.Println(c.speed)
}
func (c Car) Dash() {
	fmt.Println(c.speed * 2)
}

func CarFactory(t string, s int) Car {
	var c Car
	c.tire = t
	c.speed = s
	return c
}
