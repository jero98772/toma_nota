package main
import "fmt"
func main(){
	tableton:=12
	var num int
	fmt.Scanln(&num)
	for i:=0;i<tableton;i++{
		txt:=fmt.Sprintf("%d*%d=%d",num,i,num*i)
		fmt.Println(txt)
	}	
}