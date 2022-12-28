package main
import "fmt"
type stack []string
func (s *stack) isEmpty() bool{
	return len(*s)==0
}
func (s *stack) top() string {
	return *s[len(*s)-1]
}
func (s *stack) push(str string){
	*s=append(s*,str)
}
func (s *stack)pop(str string){
	if !s.isEmpty(){
		*s=(*s)[:s.top]
	}
}
func main(){
	var input int 
	fmt.Scanln(&input)
	var stk stack
	for i:=0;i<input;i++{
		t := strconv.Itoa(i)
		stk.push(t)
	}
}