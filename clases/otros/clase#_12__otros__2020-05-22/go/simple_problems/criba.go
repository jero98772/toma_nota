package main
import ("fmt")
func main(){
	var num int
	fmt.Scanln(&num)
	primes:=make([]int,0)
	mask:=make([]bool,num+2)
	for i:=0;i<num+2;i++{
		mask[i]=true
	}
	mask[0]=false
	mask[1]=false
	for i:=2;i<num;i++{
		if mask[i]{
			for j:=2;j*i<num;j++{
				mask[i*j]=false
			}
			primes=append(primes,i)
		}
	}
	
	fmt.Println(primes)
}