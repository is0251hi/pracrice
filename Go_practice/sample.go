package main

import mod "mymodule/sample_pl" //パッケージ前に名前付けられる、もしくは.で省略可能

func main() {
	mod.Def_normal()
	//mod.only_packageはできない
}
