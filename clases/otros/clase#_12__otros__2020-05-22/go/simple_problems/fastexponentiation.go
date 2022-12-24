package main
import "fmt"
func fexp(num,exp int)int{
	if exp==0{
		return 1
	}
	x:=fexp(num,int(exp/2))
	if exp%2==0{
		return x*x
	}else{
		return num*x*x
	}

}
func main(){
	var num,pot int
	fmt.Scanln(&num)
	fmt.Scanln(&pot)
	fmt.Println(fexp(num,pot))
}