def boslaudem():
	diasmes = 31
	valoranterior = 0
	for i in range(1,diasmes+1):
		valormin = float(input("valor minimo del cafe:  " ))
		valormax = float(input("valor maxio del cafe :  "))
		variavilidad = valormax-valormin
		if i == 0 or valormin < valoranterior and valormin < valormax:
			valoranterior = valormin
			print("valor minimo",valormin)
		else :
			print("ese valor minimo no fue el minimo")
		if i == 0 or valormax > valoranterior and valormax > valormin:
			valoranterior  = valormax
			print("valor maximo",valormax)
		else :
			print("ese valor maximo no fue el minimo")
		if  variavilidad < valoranterior :
			valoranterior  = variavilidad
			print("valor variabiliad",variavilidad,"en el dia")
		else:
			print("variabilidad no cambio",variavilidad)
	else:
		print("valor variabiliad",variavilidad,"en el dia",i)
		print("valor maximo",valormax)
		print("valor minimo",valormin)
boslaudem()
"""
En la bolsa de valores de la Universidad de Medellín, se quiere hacer un análisis
sobre el comportamiento del precio internacional de la libra de café Colombiano.
Dicho análisis se debe hacer con base en las fluctuaciones del precio
de negociación que se registraron en el mes de agosto. Para ayudar con dicho análisis
usted debe realizar un algoritmo que reciba como entradas el valor mínimo y el
valor máximo de venta de café durante los 31 días del mes. Con base en estas
entradas, usted debe indicar cual fue el precio mínimo y máximo de negociación
del café durante todo el mes. Además, debe indicar en que día del mes se presentó
la mayor variabilidad en el precio de negociación"""
    
