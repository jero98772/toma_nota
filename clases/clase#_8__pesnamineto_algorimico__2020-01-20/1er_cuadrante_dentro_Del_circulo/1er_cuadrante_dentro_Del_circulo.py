radio = int(input("radio: "))
cordenadaX = int(input("cordenda del punto en X: "))
cordenadaY = int(input("cordenda del punto en Y: "))
DistanciaPunto = (((X**2)+(Y**2))**(1/2))
print("distancia del punto es",DistanciaPunto)
if radio >= DistanciaPunto and X>0 and Y>0:
    print("esta dentro del circulo y esta en el cuadrante 1")
else:
    print("no esta en el dentro del radio o no  esta en el cuadrante 1 ")
