#import numpy as np
from datetime import datetime
import time
from pyfiglet import Figlet ,figlet_format
from pseudorandom  import prandom # para matar algunas moscas por nuestra parte 
import random# para matar otras moscas 
#forma de las fichas [valor,identificador,posicion]
def cantiadColumnas(num):# la idea es que nos diga cuantas columnas poner para las catas 	# probar  concatenado string

	nuevoNum = 1
	count = 0
	multiplicador = 2
	numMaxcolumnas = 3
	while nuevoNum <= num and count <numMaxcolumnas:
		count += 1
		if nuevoNum*multiplicador <= num: 
			nuevoNum = nuevoNum*multiplicador
	return nuevoNum
def banner():
    banner = """
    de ejm98 y jero98772
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|
un juego de memoria
  ____    _    _   _ _   _  ____   _____
 / ___|  / \  | \ | | | | |/ ___/ |  ^  |
| |     / _ \ |  \| | | | | |     | / \ |
| |___ / ___ \| |\  | |_| | |___  | \ / |
 \____/_/   \_\_| \_|\___/ \____\ |  V  |
                                   =====                                      
cartas y numeros = concentracion
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|
"""
    return banner

def advertencias():
	warnig = """
====================================
_____
\ | /  suponemos que usted sabe jugar 
 \O/   canuco es como jugar un juego                           
  v    de memoria o concetrese etc... 
_____  
\ | /  si no entiende o no juega bien 
 \O/   o pierde por la culpa del otro
  v    le recomendamos que no juege  
_____
\ | /  revise el manual del juego
 \O/   todavia no esta implementado
  v    pero tu puedes implementarlo
_____
\ | /  diseñado unicamente y pensado 
 \O/   para humanos favor no intente  
  v    si es un animal 
_____
\ | /  nesesita  cabesa y saber pensar
 \O/   para poder jugar
  v  
_____
\ | /  no pierde nada con ayudar ,ayude 
 \O/   en https://pastebin.com/JywQVZ3p
  v    (era muy largo el hypervinculo)
_____
\ | /  si quiere contribuir , contribuya
 \O/   si quiere donar , done aqui 
  v tb1qgt4trnnsxdmfcpnydkmk8ht0y4esg4cdvzmhaz
_____
\ | /  este proyecto es codigo libre ve uds 
 \O/   quien(es) trabajo en este hypervinculo 
  v    https://pastebin.com/JywQVZ3p
_____
\ | /  si por algun motivo se equivoco y
 \O/   y descargo esto dese la oportunidad 
  v    para jugar 
_____
\ | / juege disfrutando si no ,no juege
 \O/ 
  v  
_____
\ | / porfavor no critique 
 \O/  disfrute y
  v   colabore
_____
\ | / si no quiere leer no lea
 \O/  :)
  v   el juego se puede juagar solo con enter
_____
\ | / si quiere paselo a ingles
 \O/  si no entiende lo que dice paselo
  v   a lo que entienda (y pase lo que hiso)
"""	
	return warnig

def nucleo():
	f = Figlet()
	print(banner())
	print(advertencias())
	#valoresFichas = 3
	segundosEnUnMinuto = 60
	jugadores = input("cantidad de jugadores <=4 [default=2]")
	try :
		# la idea es que sea temporal un limite de jugadores
		jugadores = int(jugadores)
		if jugadores <= 4:
			quit()
	except :
		jugadores = 2
	if not jugadores:
		jugadores = 2

	cantidadFichas = input("introsca la cantidad de fichas para jugar preferible mente par el valor que va  tener por default es 20\n")
	try:
		if int(cantidadFichas) % 2== 0: #ok pasa y se puede jugar
			cantidadFichas = int(cantidadFichas)
		else :
			print("-_- te dije par eso es impar vuelve a intentar o sigues jugando con 20")
	except:
		cantidadFichas = 20
	if not cantidadFichas :
		cantidadFichas = 20	
	now = int(datetime.now().strftime('%S'))
	if now <= 10:
		now = random.randrange(10,60)#not now
	r = prandom(valorInicial = now,incrementador = 7 ,multiplicador = 1, mod = cantidadFichas/2,veces = cantidadFichas)
	#fichas = np.zeros((cantidadFichas,valoresFichas))
	#valorfichas = np.asarray(r.vector())
	valorfichas = r.vector()

	dibujofichas ="""
 _____
|  ^  |
| / \ |
| \ / |
|  V  |
 =====
	"""

	fichasRestantes = 0
	count = 0
	while fichasRestantes < cantidadFichas:
		for i in range(1,cantidadFichas+1): 
			print(dibujofichas+str(i))
		# se pueden hacer mas dde 2 jugadores y los quequiera con un for ,eval con el indicie del for concatenarlo al codigo que esta en eval 
		for i in range(1,jugadores+1):
			eleccion1= input("escoja la pocion a la que corresponde una ficha y si es mayor a la cantidad de fichas propuestas auto selcionado el valor[default=?/aleatorio][x > fichas propuestas =?/aleatorio]")
			try:
				if eleccion1 < cantidadFichas:
					eleccion1 = int(eleccion1)
			except:
				eleccion1 = random.randrange(0,cantidadFichas/2)
			if not eleccion1:
				eleccion1 = random.randrange(0,cantidadFichas/2)
			print(f.renderText(str(valorfichas[eleccion1])))
			print(eleccion1)
			eleccion2 = input("escoja la pocion a la que corresponde una ficha y si es mayor a la cantidad de fichas propuestas auto selcionado el valor[default=?/aleatorio][x > fichas propuestas =?/aleatorio]")
			try:
				if eleccion2 < cantidadFichas:
					eleccion2 = int(eleccion2)
			except:
				eleccion2 = random.randrange(0,cantidadFichas/2)
			if not eleccion2:
				eleccion2 = random.randrange(0,cantidadFichas/2)
			print(f.renderText(str(valorfichas[eleccion2])))
			print(eleccion2)
			
nucleo()
