import random
import itertools
import subprocess
subprocess.run("clear", shell =True)
print("="*75)
print(" _   juego de            ")
print("| |_ __ _ _ __ ___  __ _ ")
print("| __/ _` | '__/ _ \/ _` |")
print("| || (_| | | |  __/ (_| |")
print(" \__\__,_|_|  \___|\__,_|")
print("="*75)
print("opcion disponibles")
#main menu
dificultad = 0
vidas = 0
opcion = 0 
print("1)<--historia")
print("2)<--normal")
#game modes
opcion  = input("opcion:   ")
if not opcion :
    opcion  = "2"
try:
    opcion  = str(opcion )
except:
    opcion  = "2"
print("="*75)
print("predice el numero aleatorio")
dificultad = input("grado dificultad varia segun la cantiad de caracteres nivles de 1-99 1 basico 99 imposble:  ")
if not dificultad :
    dificultad  = 2
try:
    dificultad  = int(dificultad )
except:
    dificultad  = 2
    
vidas = input("vidas o cantidad de intentos no se potencia por 0 para evitar numeros repetidos:   ")
if not vidas :
    vidas = 7
try:
    vidas = int(vidas)
except:
    vidas = 7
print("="*75,"\n"*5)
numMisterio = random.random()
#variables and inputs lifeguards
def adivinar(numero,dificultad,numMisterio):
    numero_total = "" 
    numMisterio = str(int(numMisterio*10**dificultad))
    for num_desglosado  in numero :
        if num_desglosado in numMisterio :
            print(numero_total)
            print("acertartese ",num_desglosado,"esta en esta en el numero de " ,len(numMisterio),"cifras")
            if int(numMisterio) > int(numero):
                print("el numero ingresado es menor que el numero que nesesita encontrar")
            elif int(numMisterio) < int(numero):
                print("el numero ingresado es mayor que el numero que nesesita encontrar")
            return True
        elif str(numero) == numMisterio:
            numero_total += numero
            print("te acertartese ",numero_total)
            return False
        else :
            print("trate con otro numero ")
            print("pista")
            if int(numMisterio) > int(numero):
                print("el numero ingresado es menor que el numero que nesesita encontrar")
            elif int(numMisterio) < int(numero):
                print("el numero ingresado es mayor que el numero que nesesita encontrar")
            return True

def templatejuego(vidas,dificultad,numMisterio):
    count = 0
    numero = input("Ingrese su numero de un digito para completar el numero \nIngrese su numero :  ")
    vidas+=1
    while count <  vidas :
                 
        if count == 0 :            
            print("intentos = ",count)
            aciertos = adivinar(numero,dificultad,numMisterio)
            count += aciertos

        else:
            num = numero
            print(num)
            numero = str(input("Ingrese de nuevo un numero:  "))
            print("intentos = ",count)
            if numero == num :
                aciertos = adivinar(numero,dificultad,numMisterio)
                count += 0
            else:
                aciertos = adivinar(numero,dificultad,numMisterio)
                count += aciertos
        
            
    else :
        print("el numero era" , str(int(numMisterio*10**dificultad)))
            
#if opcion.lower() == "1" or opcion.lower() == "multijugador":
#    templatejuego()
if dificultad < 1:
        print("intentadno potenciar por 0 ,te pasas de listo  nivel 3141592653592 infinitamnte por desgraciado")
        dificultad = 314159265359
        vidas = 314159265359
        
if opcion.lower() == "1" or opcion.lower() == "historia":
    while True:
        vidas = 314159265359
        templatejuego( vidas,dificultad,numMisterio)
elif opcion.lower() == "2" or opcion.lower() == "normal":
    templatejuego(vidas,dificultad,numMisterio)

