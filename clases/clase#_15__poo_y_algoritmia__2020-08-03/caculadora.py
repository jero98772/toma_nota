import sys
from math import e ,pi ,sqrt ,exp ,log , cos, sin, tan, atan, asin ,acos
class caculadora:
	def __init__(self,expresion):
		self.expresion = expresion
	def calcular(self):
		self.entrada=eval(self.expresion)
		return self.entrada
	def contar(self):
		catidad = len(str(self.entrada))
		return catidad 
calculadora = caculadora(sys.argv[1])#input("entre algo para calcular\n"))
q = calculadora
r = q.calcular()
print()
print(q.contar())


