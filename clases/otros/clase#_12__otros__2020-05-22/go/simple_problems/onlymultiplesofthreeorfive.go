package main
import "fmt"
func main(){
	var num int
	sum:=0	
	fmt.Scanln(&num)
	for i:=0;i<num;i++{
		if i%3==0 || i%5==0{ 
			sum+=i
		}
	}
	fmt.Println(sum)
}