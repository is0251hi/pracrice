package samplepl

import "fmt"

type SuperCar struct {
	Car
}

func (s SuperCar) Gear_top() {
	fmt.Println(s.speed * 3)
}
