package main
import "fmt"
type material struct{
	name string
	amount int
	amountUnits string

}
func main(){
	graph:=make(map[material][]string)
	tierra:=material{"tierra",100,"m²"}
	graph[tierra]=[]string{"huerta","casa"}
	madera:=material{"madera",2000,"tablas"}
	graph[madera]=[]string{"huerta","silla","casa"}
	ladrillo:=material{"ladrillo",20000,"unidades"}
	miladrillo:=material{"ladrillo",100,"unidades"}
	graph[ladrillo]=[]string{"casa","silla"}
	count:=0	
	for key,_:= range graph{
		if miladrillo.name==key.name && miladrillo.amount>=key.amount{
			count+=1;
		}
		//ok:=miladrillo.name==graph[key].name && miladrillo.amount>=graph[key].amount

		fmt.Println(key)
	}
	//ok:=miladrillo.name==ladrillo.name && miladrillo.amount>=ladrillo.amount
	///if ok{
		fmt.Println(count)
	//}
		 
}