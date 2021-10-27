package samplepl

import (
	"fmt"
)

func Def_normal() {
	defer fmt.Println("finish")
	var car Car
	car.tire = "bridgestone"
	car.speed = 40
	fmt.Println(car.speed, car.tire)
	only_package()
}

func only_package() {
	println("only")
}
