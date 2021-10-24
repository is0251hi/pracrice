package main

import (
	"fmt"
)

type Car struct {
	tire  string
	speed int
}

func main() {
	var car Car
	car.tire = "bridgestone"
	car.speed = 40
	fmt.Println("Hello World")
	fmt.Println(car.speed, car.tire)
}
