radio = int(input("radio: "))
X = int(input("cordenda del punto X: "))
Y = int(input("cordenda del punto Y: "))
DistanciaPunto = (((X**2)+(Y**2))**(1/2))
print("distancia del punto es",DistanciaPunto)
if radio >= DistanciaPunto and X>0 and Y>0:
    print("esta dentro del circulo y esta en el cuadrante 1")
else:
    print("no esta en el dentro del radio o no  esta en el cuadrante 1 ")
