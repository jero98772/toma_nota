from math import *
import numpy as np
def integral(xi,xf,n,func):
	veces=1/n#(xf-xi)
	nums=np.arange(xi,xf,veces)
	applay=np.vectorize(func)
	puntos=applay(nums)
	return puntos
def main():
	print("integral desde")
	xi=int(input("desde ...\n"))
	xf=int(input("hasta ...\n"))
	n=int(input("cantidad de pasos?"))
	funcs=input("ingrese su funcion, usando x:\n")
	func=lambda x:eval(funcs)	
	puntos=integral(xi,xf,n,func)
	print(np.sum(puntos)/n)
main()