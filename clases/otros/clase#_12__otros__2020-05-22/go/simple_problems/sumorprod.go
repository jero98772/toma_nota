package main
import ("fmt"
	"strings"
)
func main(){
	var choice string
	var num int
	fmt.Println("[S] sum or [P] product:\n")
	fmt.Scanln(&choice)
	fmt.Println("input a number:\n")
	fmt.Scanln(&num)
	if strings.ToUpper(choice)=="P"{
		total:=1
		for i:=1;i<num+1;i++{
			total*=i
		}
		fmt.Println(total)
	}else if strings.ToUpper(choice)=="S"{
		total:=0
		for i:=0;i<num;i++{
			total+=i
		}
		fmt.Println(total)
	}else{
		fmt.Println("invalid choice")
	}
}