package main
import "fmt"
func multable(num int){
	for i:=0;i<12;i++{
		txt:=fmt.Sprintf("%d*%d=%d",num,i,num*i)
		fmt.Println(txt)
	}
}
func main(){
	tableton:=12
	for i:=0;i<tableton;i++{
		multable(i)
		fmt.Println("-------")
	}	
}