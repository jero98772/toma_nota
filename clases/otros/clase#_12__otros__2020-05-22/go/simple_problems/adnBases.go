package main
import "fmt"
func main(){
	bases:=make(map[rune]int)
	var chain string
	fmt.Scanln(&chain)
	for _,char:= range chain{
		//fmt.Println(char)
		_,is:=bases[char]		
		if is{
			bases[char]+=1			
		}else{
			bases[char]=1
		}
	}
	fmt.Println(bases)
}