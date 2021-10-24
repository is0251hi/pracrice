package samplepl

import (
	"fmt"
)

func Def_normal() {
	var car Car
	car.tire = "bridgestone"
	car.speed = 40
	fmt.Println(car.speed, car.tire)
}
