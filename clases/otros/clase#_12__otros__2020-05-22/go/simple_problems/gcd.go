package main
import "fmt"
func gdc(a,b int)int{
	if b==0{
		return a
	}else{
		return gdc(b,a%b)
	}
}
func main(){
	var num1,num2 int
	fmt.Scanln(&num1)
	fmt.Scanln(&num2)
	fmt.Println(gdc(num1,num2))

}