from math import *

def integral(xi,xf,n,func):
	veces=(xf-xi)//n
	print(xi,xf,veces)
	nums=list(range(xi,xf,veces))
	puntos=list(map(func,nums))
	return puntos
def main():
	print("integral desde")
	xi=int(input("desde ..."))
	xf=int(input("hasta ..."))
	n=int(input("cantidad de pasos?"))
	
	funcs=input("ingrese su funcion, usando x")
	func=lambda x:x+1#eval(funcs)	
	
	puntos=integral(xi,xf,n,func)
	print(puntos)
	print(sum(puntos))
main()