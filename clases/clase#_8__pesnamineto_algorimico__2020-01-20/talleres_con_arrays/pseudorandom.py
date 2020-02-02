""" 
m modulo 
a multiplicador
c incremento
X0 valor inicial
X valor
xn+1 = (axn + c) mod m
"""
class random:
    def help():
        
    def matrix():
    valor = 9
    mod = 600
    incrementador = 10
    multiplicador = 8
    veces = 100
    contador=0
    while valor < mod and veces>contador:
        valor =(multiplicador * valor + incrementador) % mod
        contador+=1    
        print(contador,"\t",valor)
#continuara despues