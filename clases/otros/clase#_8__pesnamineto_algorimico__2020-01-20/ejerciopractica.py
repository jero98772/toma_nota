"""un alamcen efcutua una promocion segun el color de la bola que saca en la caja
si la bola es blaca no hay descuento
verde 10%
amarilla 25%
azul 50%
roja 100%"""
try :
    valorcompra = eval(input("precio de la compra:  "))
    bola = str(input("bola \n 1) blanaca  \n 2) verde 10% \n 3) amarilla 25% \n 4) azul 50% \n 5) rojo 100% \n"))
    if bola == "blanca".lower() or bola == "1":
        valorfinal = valorcompra

    elif bola == "verde".lower() or bola == "2":
        valorfinal  = valorcompra * 0.10

    elif bola == "amarilla".lower() or bola == "3":
        valorfinal  = valorcompra * 0.25

    elif bola == "azul".lower() or bola == "4":
        valorfinal  = valorcompra * 0.50

    elif bola == "rojo".lower() or bola == "5":
        valorfinal  = 0
    print("pagas",valorfinal)
except:
    print("intenta con un un numero de 1 a 5")
    print("jaja no te dio cuidado manito")
