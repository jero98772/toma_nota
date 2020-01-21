#comentario se usa para notas o desactivar fragmentos de codigo
"""comentario multilinea"""
import time
import math
PI=math.pi
#importar librerias
distancia=0
tiempo=0
giro=0
radio=PI*1# o 3.14159265359
#giro,distancia y tiempo son numeros enteros
#los numeros enteros son los - y +
velocidad =0.0
#velocidad es un valor flotante/decimal eso es una division
#on_off= False
modelo=""
#las varles deben ser en lo posibles faciles de escribir y entendibles y acorde la funcionalidad de la varible
#en un codigo hay que pensar en el otro como usuario
def prender():
    on_off=False
    while on_off ==False:
        on_off=True
        return on_off
prender=prender()

print("estado del motor prendido:" ,prender)
class mov:
    def movimiento():
        lista_giro=[]
        for giro in range(361):
            print("giro",giro)
            lista_giro.append(giro)
        return lista_giro

#print(movimiento)
def velocidad(opcion,radio):
    movimiento=mov.movimiento()
    vel_lista=[]
    diametro=radio*2
    for i in movimiento:
        #print(i)
        repeticiones=i/360
        #print(repeticiones)
        vel=repeticiones*100
        #print(vel)
        vel_lista.append(vel)
    for V in vel_lista[1:]:
        tiempo=diametro/V
        #print(tiempo)
    if opcion == "aumentar":
        #para que de una vueta en un "segundo"
        for i in range(int(vel+1)):
            aumentar=diametro*i
            #print(aumentar)
            return aumentar
    elif opcion == "disminuir":
        for i in range(int(vel+1)):
            i_lista=[]
            i_lista.append(i)
            #print("debug1")
            print(i_lista)
    elif opcion == "mantener":
        velocidad=int(input("\t seleccine si velocidad\n"))
        num=100
        for i in range(60*5):
            time.sleep(0.1)
            print(velocidad,"\tlleva",i/60,"del tiempo")
            print("  M")
            print("0(M)0")

            while not  i/num ==0 :
            	print("   M")
            	print(" 0(M)0")
            	num*=2
    else:
    	print("selecciona otra opcion")
    	
op1="disminuir"
op2="aumentar"
op3="mantener"
time.sleep(0.25)
velocidad(op3,radio)
movimiento=mov.movimiento()
print("un codigo para aprednder a progrmar")
