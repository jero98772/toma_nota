""" 
m modulo 
a multiplicador
c incremento
X0 valor inicial
X valor
xn+1 = (axn + c) mod m
"""
class random(valor = 3, mod = 600 ,incrementador = 10,multiplicador = 7 ,veces=1):
	self.valor = valor #valor  inicial para ir aumentandolo y disminuyendo
	self.mod = mod
	self.incrementador = incrementador
	self.multiplicador = multiplicador
	self.veces = veces #veces para que salgan numeros "aleatorios" o tamaño del la lista 
	self.array = []
    def matrix(self):
    	self.contador = 0
	    while self.valor < self.mod and self.veces > self.contador:
	        self.valor = (self.multiplicador * self.valor + self.incrementador) % self.mod
	        self.contador += 1
	        self.array.append(self.valor)    
	        #print(contador,"\t",valor)
	        return self.array
	def digito(self):
		self.digito = self.array[valor]
		return self.digito
	def help():
        print("formula\n m modulo \n  a multiplicador \n c incremento \n X0 valor inicial \n X valor \n xn+1 = (axn + c) mod m")
        print("m>0 \n  m>a>0 \n m>c>0")
#continuara despues