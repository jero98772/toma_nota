from math import atan2
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanciaAlOrigen(self):
      dist=(self.x**2+self.y**2)**(1/2)
      print(round(dist,2))
    
    def anguloConElEjeX(self):
       print(round(atan2(self.y,self.x),2))
    
    def distanciaAOtroPunto(self, punto2):
      dist=((punto2.x-self.x)**2+(punto2.y-self.y)**2)**(1/2)  
      print(round(dist,2))

# INPUT
x1, y1 =  map(int, input().split())
x2, y2 =  map(int, input().split())

punto1 = Punto(x1, y1)
punto2 = Punto(x2, y2)

punto1.distanciaAlOrigen()
punto1.anguloConElEjeX()
punto1.distanciaAOtroPunto(punto2)