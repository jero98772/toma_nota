import sys
from random import  random ,randint ,randrange
#from math import e ,pi ,sqrt ,exp , log, log10  ,log2, cos, sin, tan, atan, asin ,acos, pow ,atan2 ,hypot,degrees,radians
#o
from  math import * 
class caculadora:
	def __init__(self,expresion):
		self.expresion = expresion
	def calcular(self):
		self.entrada=eval(self.expresion)
		return self.entrada
	def contar(self):
		catidad = len(str(self.entrada))
		return catidad
calculadora = caculadora(input("entre algo para calcular\n")) 
#calculadora = caculadora(sys.argv[1])#input("entre algo para calcular\n"))
q = calculadora
r = q.calcular()
print(r)
print("digitos de la solucion" , q.contar())


