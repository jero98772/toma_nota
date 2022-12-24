//b==0
package main
import "fmt"
func main(){
	var num1,num2 int
	fmt.Scanln(&num1)
	fmt.Scanln(&num2)
	for num2>=1{
		tmp:=num1
		num1=num2
		num2=tmp%num2
		}
	fmt.Println(num1)
}