package main

import "fmt"

func main() { 
	var a chan int
	if a ==nil{
		fmt.Println("chanel is empty")
		a=make(chan int)
		fmt.Println("type of chanel %T",a)	
	}
}