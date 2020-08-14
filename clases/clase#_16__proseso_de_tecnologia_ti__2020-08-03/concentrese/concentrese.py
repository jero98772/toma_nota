import numpy as np
from datetime import datetime
from pseudorandom  import prandom
#forma de las fichas [valor,identificador,posicion]
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

r = prandom(valorInicial = now,incrementador = now ,multiplicador = 1, mod = cantidadFichas/2,veces = cantidadFichas)
valoresFichas = 3
fichas = np.zeros((cantidadFichas,valoresFichas))
valorfichas = np.asarray(r.vector())
#for i in cantidadFichas:
#for j in valoresFichas:
#fichas[i][0] =
print(valorfichas) 
#print(fichas)