try :
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
    print("peligro no es un programa educativo")
    print("1)<--historia")
    print("2)<--normal")
    #print("3)<--multijugador")
    opcion  = input("opcion:   ")
    print("="*75)
    print("predice el numero aleatorio")
    dificultad = int(input("grado dificultad varia segun la cantiad de caracteres nivles de 1-99:  "))
    vidas = int(input("vidas:   "))
    
    print("="*75,"\n"*5)
    numMisterio = random.random()
    def adivinar(numero,dificultad,numMisterio):
        numero_total = "" 
        numMisterio = str(int(numMisterio*10**dificultad))
        if str(numero) == numMisterio:
            numero_total += numero
            print("te acertartese ",numero_total)
            return False
        else :
            print("trate con otro numero ")
            return True
        for num_desglosado ,i in itertools.product(numero ,range(len(numero))):
            if num_desglosado in numMisterio :
                print(numero_total)
                print("acertartese ",num_desglosado,"esta en la posion",i)
            return True 
    def templatejuego(vidas,dificultad,numMisterio):
        count = 0
        numero = str(input("Ingrese su numero de un digito para completar el numero \nIngrese su numero :  "))
        vidas+=1
        while count <  vidas or  vidas  == 1j:
                     
            if count == 0 :            
                print("intentos = ",count)
                aciertos = adivinar(numero,dificultad,numMisterio)
                count += aciertos
            else:
                numero = str(input("Ingrese de nuevo un numero:  "))
                aciertos = adivinar(numero,dificultad,numMisterio)
                print("intentos = ",count)
                count += aciertos
               
                
        else :
            print("el numero era" , str(int(numMisterio*10**dificultad)))
                
    #if opcion.lower() == "1" or opcion.lower() == "multijugador":
    #    templatejuego()
    if dificultad < 1:
            print("intentadno potenciar por 0 ,te pasas de listo  nivel 3141592653592 infinitamnte por desgraciado")
            dificultad = 3141592653592
            vidas = 3141592653592
    if opcion.lower() == "1" or opcion.lower() == "historia":
        while True:
            vidas = 3141592653592
            templatejuego( vidas,dificultad,numMisterio)
    elif opcion.lower() == "2" or opcion.lower() == "normal":
        templatejuego(vidas,dificultad,numMisterio)

except:
    numMisterio = random.random()
    print("tramposo quiere jugar  ")
    jugar=input("si) jugar\n y afrontar sus consecunecias  ")
    if jugar.lower() == "si":
        print("igual mente es involuntario")
        
        for i in range(int(numMisterio*10**3)) :
            print(bin(11**10**6))
            print("jajajajajajajaja"*10+"k")

            try :
                exit()
            except:  
                print(bin(11**10**6))
                print("jajajajajajajaja"*10+"k")
    else:
        contartaque = "start "
        for i in range(int(numMisterio*10**2)) :
            print(bin(11**10**6))
            subprocess.run("clear", shell =True)
            print("jajajajajajajaja"*10+"k")
            contartaque *= 9
            try :
                exit()
            except:
                contartaque *= 90
                print(bin(11**10**6))
                print("jajajajajajajaja"*10+"k")
                subprocess.run("@echo off\n", shell =True)
    print("muy gracioso verda ...")
