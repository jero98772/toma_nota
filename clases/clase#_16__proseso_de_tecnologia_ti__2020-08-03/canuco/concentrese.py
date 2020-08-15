import numpy as np
from datetime import datetime
import time
from pseudorandom  import prandom # para matar algunas moscas por nuestra parte 
import random # para matar otras moscas 
#forma de las fichas [valor,identificador,posicion]

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
def main():
	print(banner())
	valoresFichas = 3
	segundosEnUnMinuto = 60
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
	#now = int(datetime.now().strftime('%S'))
	now = 0
	if now == 0:
		now = random.randrange(1,60)#not now
	r = prandom(valorInicial = now,incrementador = now ,multiplicador = 1, mod = cantidadFichas/2,veces = cantidadFichas)
	fichas = np.zeros((cantidadFichas,valoresFichas))
	valorfichas = np.asarray(r.vector())
	dibujofichas ="""
 _____
|  ^  |
| / \ |
| \ / |
|  V  |
 =====
	"""
	for i in range(1,cantidadFichas+1): 
		print(dibujofichas+str(i))
	#print(valorfichas) 
main()