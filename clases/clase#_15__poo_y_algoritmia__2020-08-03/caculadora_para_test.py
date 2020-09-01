import sys
from math import e ,pi ,sqrt ,exp ,log , cos, sin, tan, atan, asin ,acos
class caculadora:
	__atributoPI__ = 3.1415926535
	def __init__(self,expresion):
		self.expresion = expresion
	def __sumarle2__(self):
		return self.expresion +"2"
	def sumarle2publica(self):
		return self.expresion +"2"
	def calcular(self):
		entrada=eval(self.expresion)
		return entrada
calculadora = caculadora(sys.argv[1])#input("entre algo para calcular\n"))
r = calculadora.calcular()
print(r)
loPrivado = calculadora.__atributoPI__
mas2 = calculadora.__sumarle2__()
sumarle2publica = calculadora.sumarle2publica()
print("lo que emtiendo por lo que es privado/protegido e python ",loPrivado,"y que le sume mas 2 en un metodo 'pivado '",mas2,"y que le sume mas 2 en un metodo 'publico '",sumarle2publica)
calculadora.__atributoPI__ = pi
loPrivadoprobado = calculadora.__atributoPI__
print("lo que emtiendo por lo que es privado/protegido e python ",loPrivadoprobado,"no deberia cambiar")

