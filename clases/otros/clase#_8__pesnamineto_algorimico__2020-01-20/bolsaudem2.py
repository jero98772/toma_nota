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
