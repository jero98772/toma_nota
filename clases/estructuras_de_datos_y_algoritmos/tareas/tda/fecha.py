#Modifica el Fraccionario f1 sin problema, volvera a su valor original
def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

class Fraccionario:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def mostrar(self):
        return a/b
    
    def sumar(self, fraccionario2):
         return (self.a*fraccionario.b+self.b*fraccionario2.a)/fraccionario2.b*self.b
    
    def restar(self, fraccionario2):
        
    
    def multiplicar(self, fraccionario2):
        
    
    def dividir(self, fraccionario2):
    

# Toma de datos e impresion
x, y = map(int, input().split())
f1 = Fraccionario(x, y)

a, b = map(int, input().split())
f2 = Fraccionario(a, b)

# Original
print()f1.mostrar())

# Al sumar
f1.sumar(f2)
print(f1.mostrar())
f1 = Fraccionario(x, y)


# Al restar
print(f1.restar(f2))
f1.mostrar()
f1 = Fraccionario(x, y)


# Al multiplicar
f1.multiplicar(f2)
f1.mostrar()
f1 = Fraccionario(x, y)

# Al dividir
f1.dividir(f2)
f1.mostrar()
