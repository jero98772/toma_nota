package main
import "fmt"
type maxheap struct{
	array []int
}
func (h *maxheap) Insert(val int){
	h.array=append(h.array,val)
	h.maxHeapifyUp(len(h.array)-1)
}
func (h *maxheap) maxHeapifyUp(index int){
	for h.array[parent(index)]<h.array[index]{
		h.swap(parent(index),index)
		index=parent(index)
	}
}
func parent(i int) int{
	return (i-1)/2
}
func left(i int) int{
	return 2*i+1
}
func rigth(i int) int{
	return 2*i+2
}
func (h *maxheap) swap(i1,i2 int){
	h.array[i1],h.array[i2]=h.array[i2],h.array[i1]
}
func (h *maxheap) insert(val int){
	h.array=append(h.array,val)
	h.maxheapify(len(h.array)-1)
}
func main(){
	m:=&maxheap{}
	fmt.Println(m)
	
}