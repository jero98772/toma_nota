from math import *

def integral(xi,xf,n,func):
	veces=1/n#(xf-xi)
	#print(xi,xf,veces)
	nums=list(range(xi,xf,veces))
	puntos=list(map(func,nums))
	return puntos
def main():
	print("integral desde")
	xi=int(input("desde ...\n"))
	xf=int(input("hasta ...\n"))
	n=int(input("cantidad de pasos?"))
	
	funcs=input("ingrese su funcion, usando x:\n")
	func=lambda x:eval(funcs)	
	
	puntos=integral(xi,xf,n,func)
	print(puntos)
	print(sum(puntos))
main()