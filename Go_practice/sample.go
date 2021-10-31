package main

import (
	"fmt"
	mod "mymodule/sample_pl"
) //パッケージ前に名前付けられる、もしくは.で省略可能

func main() {
	var (
		s int
		t string
	)
	mod.Def_normal()
	//mod.only_packageはできない
	fmt.Scanf("speed:", &s)
	fmt.Scanf("tire:", &t)
	var car = mod.CarFactory(t, s)
	var c mod.Handle = car
	var s_car mod.SuperCar = mod.SuperCar{
		Car: car,
	}
	s_car.Dash()
	c.Run()
	c.Dash()
}
