#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
import random
import numpy as np
import time
import subprocess

def palabra_aleatoria():
    """
    Genera una palabra aleatorio leida desde un archivo
    :return: str la palabra generada
    """

    with open("words.txt", "r") as f:
        data = f.readlines()

    n = random.randint(0, len(data)-1)
    return data[n].replace("\n","").lower()


def dibujar_ahorcado(partes):
    """
    Dibuja el muñeco del ahorcado con base en la partes dadas
    :param partes: las partes del muñeco que se van a dibujar
    1: cabeza
    2: cabeza y cuerpo
    3: cabeza, cuerpo y un brazo
    4: cabeza, cuerpo y ambos brazos
    5: cabeza, cuerpo, ambos brazo y una pierna
    6: cabeza, cuerpo, ambos brazos y ambas piernas
    """
    print("{:_^10}".format(""))
    print("{:>10}".format("|"))

    if partes == 1:
        print("{:>11}".format("(_)"))
    elif partes == 2:
        print("{:>11}".format("(_)"))
        print("{:>10}".format("|"))
        print("{:>10}".format("|"))
        print("{:>10}".format("|"))
    elif partes == 3:
        print("{:>11}".format("(_)"))
        print("{:>10}".format("|"))
        print("{:>10}".format("/|"))
        print("{:>10}".format("|"))
    elif partes == 4:
        print("{:>11}".format("(_)"))
        print("{:>10}".format("|"))
        print("{:>11}".format("/|\\"))
        print("{:>10}".format("|"))
    elif partes == 5:
        print("{:>11}".format("(_)"))
        print("{:>10}".format("|"))
        print("{:>11}".format("/|\\"))
        print("{:>10}".format("|"))
        print("{:>10}".format("/ "))
    elif partes == 6:
        print("{:>11}".format("(_)"))
        print("{:>10}".format("|"))
        print("{:>11}".format("/|\\"))
        print("{:>10}".format("|"))
        print("{:>11}".format("/ \\"))

    print("\n")
def gameover():
		print(" try again \n ... \n")
		time.sleep(2)
		print("  game over ")
		time.sleep(1)
		print("sorry men")
		time.sleep(1)
		for i in range(3):
			print(". \n")
			time.sleep(1)
def adorno():
	subprocess.run("clear", shell =True)
	print('| .__________))______|          ')
	print('| | / /      ||          ')
	print('| |/ /       ||          ')
	print('| | /        ||.-''.          ')
	print('| |/         |/  _  \          ')
	print('| |          ||  `/,|          ')
	print('| |          (\\`_.           ')
	print('| |         .-`-- .          ')
	print('| |        /Y . . Y\          ')
	print('| |       // |   | \\          ')
	print('| |      //  | . |  \\          ')
	print('| |     ()   |   |   (`         ')
	print('| |          ||"||         ')
	print('| |          || ||         ')
	print('| |          || ||         ')
	print('| |          || ||         ')
	print('| |         / | | \         ')
	print('""""""""""|_`-'   ' |"""|         ')
	print('|"|"""""""\ \        "|"|         ')
	print('| |        \ \        | |         ')
	print(': :         \ \       : :            ')
	print('. .          `""       . .         ')
	print(" _                                             ")
	print("| |                                            ")
	print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
	print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
	print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
	print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
	print("                    __/ |                      ")
	print("                   |___/                       ")
	opciones = input("""
selecione un modo de juego
(A)todo o Nada ,te sacrificas por adivinar la palabra completa
(1) letra ,poner solo 1 letra 
(C)rear palabra ,sirve para juegos multijugador
(E)salir
======================================================================
select a game mode
(A) all or nothing, you sacrifice yourself for guessing the complete word
(1) letter, put only 1 letter
(C)reate word, good for multiplayer games
(E)xit
""").lower()
	return opciones
def adivinar(rndpalabra, palabracompleta):
	#print(rndpalabra)#shhhhhhh
	#palabracompleta = input("enter the word:  ").lower()
	if str(rndpalabra) == str(palabracompleta):# las palabras traen un salto de linea por defecto
		print("correct, the word was",rndpalabra)
	else :
		gameover()
		print(rndpalabra+" and you say "+palabracompleta)
def continuacion(opciones):
	continuacion = input("play again?[Y/N] or play (O)ther:  ").lower()
	if continuacion == "y":
		return opciones, palabra_aleatoria()
		adorno()
	elif continuacion == "n":

		exit()
	elif continuacion == "o":
		opciones = adorno()
		return opciones ,palabra_aleatoria() 
def win(acumulado,rndpalabra,count):
	logro = ""
	for win in acumulado:
		logro+=win
	if rndpalabra == logro:
		name = input("Congratulations you win, Remember me your name?:   ")
		print("""
	                     __                     __                   _ 
	 _   _  ___  _   _  | _|_      _____   _ __|_ |   __ _ _ __   __| |
	| | | |/ _ \| | | | | |\ \ /\ / / _ \ | '_ \| |  / _` | '_ \ / _` |
	| |_| | (_) | |_| | | | \ V  V / (_) || | | | | | (_| | | | | (_| |
	 \__, |\___/ \__,_| | |  \_/\_( )___( )_| |_| |  \__,_|_| |_|\__,_|
	 |___/              |__|      |/    |/     |__|                    
	                         _                                                    
	 _ __ ___ _ __ ___   ___| |__   ___ _ __   _   _  ___  _   _    __ _ _ __ ___ 
	| '__/ _ \ '_ ` _ \ / _ \ '_ \ / _ \ '__| | | | |/ _ \| | | |  / _` | '__/ _ \   
	| | |  __/ | | | | |  __/ |_) |  __/ |    | |_| | (_) | |_| | | (_| | | |  __/
	|_|  \___|_| |_| |_|\___|_.__/ \___|_|     \__, |\___/ \__,_|  \__,_|_|  \___|
	                                           |___/                              
	         _                                             
	  __ _  | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
	 / _` | | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
	| (_| | | | | | (_| | | | | (_| | | | | | | (_| | | | |
	 \__,_| |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
	                           |___/                       
	""",name, "you find", acumulado," in  hangman with",count ,"fails")
	else:	
		gameover()
def templatejuego():
	rndpalabra = palabra_aleatoria()
	rndpalabra = rndpalabra.lower()
	turn = True
	count = 0
	vidas = 6
	logro = ""
	arr = np.chararray(len(rndpalabra ))
	acumulado = np.chararray(len(rndpalabra ),unicode=True)
	arr[:] = " "
	letrasfallos = "fails  "
	letras = [letras for letras  in  rndpalabra]
	acumulado[:] =  "-"
	opciones = adorno()
	try:
		opciones = opciones
	except:
		opciones = "1"
	while turn:

		if opciones == "e":
			exit()
			turn = False
		while opciones == "c":

			rndpalabra =input("enter the word so that your operator does not guess:  ").lower()
			arr = np.chararray(len(rndpalabra ))
			acumulado = np.chararray(len(rndpalabra ),unicode=True)
			arr[:] = " "
			letrasfallos = ""
			letras = [letras for letras  in  rndpalabra]
			acumulado[:] =  "-"
			opciones = adorno()
		while opciones == "a" :
			print("have ",len(rndpalabra)," leters")
			palabracompleta = input("enter the word:  ").lower()
			adivinar(rndpalabra,palabracompleta)
			opciones , rndpalabra = continuacion(opciones)
		while opciones == "1" and count<vidas :
			print("lifes:",vidas-count,"\t",letrasfallos)
			print(acumulado)	

			dibujar_ahorcado(count)	
			if count == 0:
				letra = input("what letter are you going to try ")
				if len(letra) == 1:
					for i in range(len(letras)):
						if  str(letra) == str(letras[i]):
							acumulado[i] = letras[i]
					else:		
						#if   (str(letra)  in acumulado[i]):
						if not( letra in letras):
							count += 1
							letrasfallos +=str(letra)

#en un juego normal no se adivina la palabra de 1 un intento por eso esta la opacion a que es otro tipo de juego

				else: count += 1; print("cheat for that is modality a or try it after the first turn")	

			elif 0<count<vidas :
				letra = input("what letter are you going to try ")
				if len(letra) == 1:
					for i in range(len(letras)):
						if  str(letra) == str(letras[i]):
							acumulado[i] = letras[i]
					else:		
						#if   (str(letra)  in acumulado[i]):
						if not( letra in letras):
							count += 1
							letrasfallos +="-"+str(letra)
				elif len(letra) > 1:
					decion = input("try all or nothing, you sacrifice yourself for guessing the complete word [Y/N], you can't take back:  ").lower()
					if decion == "y":
							adivinar(rndpalabra,letra)
							opciones , rndpalabra = continuacion(opciones)
							count = 0
							logro = ""
							arr = np.chararray(len(rndpalabra ))
							acumulado = np.chararray(len(rndpalabra ),unicode=True)
							arr[:] = " "
							letrasfallos = "fails "
							acumulado[:] =  "-"
							letras = [letras for letras  in  rndpalabra]
					elif decion == "n":pass
					else: count += 1		
			if  "-" not in acumulado:
				print(letrasfallos)
				print(acumulado)	
				dibujar_ahorcado(count)	
				win(acumulado,rndpalabra,count)
				opciones , rndpalabra = continuacion(opciones)			
				count = 0
				logro = ""
				arr = np.chararray(len(rndpalabra ))
				acumulado = np.chararray(len(rndpalabra ),unicode=True)
				arr[:] = " "
				letrasfallos = "fails "
				acumulado[:] =  "-"
				letras = [letras for letras  in  rndpalabra]

		while not ( count<vidas) :
			print(letrasfallos)
			print(acumulado)	
			dibujar_ahorcado(count)		
			print("game over ,the word is",rndpalabra)	
			count = 0
			logro = ""
			opciones , rndpalabra = continuacion(opciones)	
			arr = np.chararray(len(rndpalabra ))
			acumulado = np.chararray(len(rndpalabra ),unicode=True)
			arr[:] = " "
			letrasfallos = "fails "
			acumulado[:] =  "-"
			letras = [letras for letras  in  rndpalabra]
templatejuego()
