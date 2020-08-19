import numpy as np
from pyfiglet import Figlet ,figlet_format
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
def turnos(valorfichas,turnosxjugaor,cantidadFichas,puntosJugador,fichasNoRestantes,fichasExcluidas):
	f = Figlet()
	eleccion1 = input("escoja la pocion a la que corresponde una ficha y si es mayor a la cantidad de fichas propuestas auto selcionado el valor[default=?/aleatorio]\n[x > fichas propuestas =?/aleatorio]\n[ficha anterior mente selcionado =?/aleatorio]\n[ficha no entendida = ?/aleatorio]\n[ficha que no sea un numero > 0 = ?/aleatorio]")
	try:
		if eleccion1 < cantidadFichas:
			eleccion1 = int(eleccion1)
	except:
		eleccion1 = int(random.randrange(0,cantidadFichas))
		while eleccion1 in fichasExcluidas:
			eleccion1 = int(random.randrange(0,cantidadFichas))
	if not eleccion1:
		eleccion1 = int(random.randrange(0,cantidadFichas))
		while eleccion1 in fichasExcluidas:
			eleccion1 = int(random.randrange(0,cantidadFichas))

	print(f.renderText(str(valorfichas[eleccion1])))
	print(eleccion1+1)
	eleccion2 = input("escoja la pocion a la que corresponde una ficha y si es mayor a la cantidad de fichas propuestas auto selcionado el valor[default=?/aleatorio]\n[x > fichas propuestas =?/aleatorio]\n[ficha anterior mente selcionado =?/aleatorio]\n[ficha no entendida = ?/aleatorio]\n[ficha que no sea un numero > 0 = ?/aleatorio]")
	try:
		if eleccion2 < cantidadFichas and eleccion2 in fichasExcluidas:
			eleccion2 = int(eleccion2)			
	except:
		eleccion2 = int(random.randrange(0,cantidadFichas))
		while eleccion2 in fichasExcluidas:
			eleccion2 = int(random.randrange(0,cantidadFichas))

	if not eleccion2:
		eleccion2 = int(random.randrange(0,cantidadFichas))
		while eleccion1 in fichasExcluidas:
			eleccion1 = int(random.randrange(0,cantidadFichas))

	print(f.renderText(str(valorfichas[eleccion2])))
	print(eleccion2+1)
	if eleccion1 != eleccion2 and valorfichas[eleccion1] == valorfichas[eleccion2] and valorfichas[eleccion1] != False and valorfichas[eleccion2] != False :
		puntosJugador =+ 1
		valorfichas[eleccion1] = False
		valorfichas[eleccion2] = False
		fichasNoRestantes =+ 2
		fichasExcluidas.append(valorfichas[eleccion1])
		fichasExcluidas.append(valorfichas[eleccion2])
		return puntosJugador , valorfichas , fichasNoRestantes ,fichasExcluidas
	else:
		return puntosJugador , valorfichas , fichasNoRestantes ,fichasExcluidas

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
_____
\ | / respetico con el amigito 'concentrese.py'
 \O/  por lo menos sabe majejar los problemas
  v   es diferente a nosotros puede ser mejor
"""	
	return warnig
def opciones():
	texto = banner()+"""
=================================================
opciones modos de juego y cosas a tener en cuenta
[0] - manual de juego
[1] - advertecias 
[2] - ver banner
[3] - jugar
[opcion predeterminada ]= 3
	"""
	return texto
def manual():
	texto = """
nadie escribio nada ni hiso nada ni leyo lo que esta escrito si quiere usted puede hacer algo en el repo
https://github.com/jero98772/creador_y_administrador_de_carpetas_y_archivos_para_tomar_nota/tree/master/clases/clase%23_16__proseso_de_tecnologia_ti__2020-08-03/canuco
	"""
	return texto
def graciasA():
	texto = """
nadie hiso nada si usted quiere saber quien trabajo y dejo registro
puede ir a ver a https://github.com/jero98772/creador_y_administrador_de_carpetas_y_archivos_para_tomar_nota/tree/master/clases/clase%23_16__proseso_de_tecnologia_ti__2020-08-03/canuco
a ver si alguien realmente hiso algo
	"""
	return texto		
def nucleo():
	# quitar o restar la cantidad de cartas a imprimir (poner nuevos indices para las cartas o saltarlos) y evitar que la gente llege y vuelva a colocar esos indices y cambiar la cantidad  de numeros aleatorios puede ser con rnd - 
	fichasExcluidas = []
	print(banner())
	#valoresFichas = 3
	segundosEnUnMinuto = 60
	puntosJugador1 = 0
	puntosJugador2 = 0 
	cantidadFichas = input("introduzca la cantidad de fichas para jugar preferible mente par el valor que va  tener por default es 20\n")
	try:
		if int(cantidadFichas) % 2== 0: #ok pasa y se puede jugar
			cantidadFichas = int(cantidadFichas)
		else :
			print("-_- te dije par eso es impar vuelve a intentar o sigues jugando con 20")
	except:
		cantidadFichas = 20
	if not cantidadFichas :
		cantidadFichas = 20	
	#fichas = np.zeros((cantidadFichas,valoresFichas))
	#valorfichas = np.asarray(r.vector())
	larry1 = np.arange(cantidadFichas/2)
	larry2 = np.arange(cantidadFichas/2)
	valoresfichasnp1 = np.concatenate((larry1 , larry2), axis=None)
	np.random.shuffle(valoresfichasnp1)
	valorfichas = valoresfichasnp1.tolist()

	dibujofichas ="""
 _____
|  ^  |
| / \ |
| \ / |
|  V  |
 =====
	"""
	turnosxjugaor = 2
	fichasNoRestantes = 0
	count = 0
	turno = 1
	print("empiesa el jugador1 ,\n los turnos del jugador 1 son impares \n los turnos del jugador 2 son pares")
	while fichasNoRestantes < cantidadFichas:
		for i in range(1,cantidadFichas+1):
			if valorfichas[i-1] in fichasExcluidas : 
				print(dibujofichas+str(i))
		# se pueden hacer mas de 2 jugadores y los quequiera con un for ,eval con el indicie del for concatenarlo al codigo que esta en eval 
		# hasta que se pare de sacar un  par paren los turnos  
		print(valorfichas)
		if turno % 2 == 0 :
			print("turno ",turno ," es para el jugador 2")
			puntosJugador2 , valorfichas , fichasNoRestantes , fichasExcluidas= turnos(valorfichas,turnosxjugaor,cantidadFichas, puntosJugador2 ,fichasNoRestantes, fichasExcluidas)
		else:
			print("turno ",turno ," es para el jugador 1")
			puntosJugador1 , valorfichas , fichasNoRestantes , fichasExcluidas= turnos(valorfichas,turnosxjugaor,cantidadFichas, puntosJugador1 ,fichasNoRestantes, fichasExcluidas)

		turno += 1
def main():
	print(opciones())
	selecion = input("\n")
	try:
		selecion = str(selecion)
	except:
		selecion = "3"
	if not selecion:
		selecion = "3"
	if selecion == "0":
		print(manual())
	elif selecion == "1":
		print(advertencias())
	elif selecion == "2":
		print(banner())
	elif selecion == "3":
		nucleo()

if __name__=='__main__':
	main()
