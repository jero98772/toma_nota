import datetime
def dias29feb(años):
	diasX29feb = int(años) // 4
	return  diasX29feb 
def fechaStr2Arr(fecha):
	fechaArr = []
	tmp = ""
	for i in str(fecha):
		if i == "-":
			fechaArr.append(tmp)
			tmp = ""
		else :
			tmp += i
	else: 
		fechaArr.append(tmp)
	return fechaArr
def diasXmes(mes):
	esMesesCon31dias = [True,False,True,False,True,False,True,True,False,True,False,True]
	dias = 0
	for i,j in zip(esMesesCon31dias,range(int(mes-1))):
		if i:
			dias += 31
		elif j == 1:
			dias += 28
		else:
			dias += 30
	return dias
def diasTotales(dia):
	#hoy = fechaStr2Arr("0000-09-13")
	#hoy = fechaStr2Arr(str(datetime.datetime.today().strftime('%Y-%m-%d')))
	dia = fechaStr2Arr(dia)	
	print(dia)
	años = int(dia[0])
	print(años)	
	añosTotales = años * 365
	print(añosTotales)
	meses = int(dia[1])
	print(meses)
	dias = int(dia[2])
	print(dias)
	diasDeMeses = diasXmes(meses)
	print(diasDeMeses)
	if años == 0:
		diasTotales =  diasDeMeses + dias
	else:	
		dias += dias29feb(años)
		print(dias)
		diasTotales = añosTotales + dias + diasDeMeses 
	return diasTotales
nueva = "2019-09-30"
antigua = "2018-09-20"
def diferneciaFecha(antigua,nueva):
	diasAntigua = diasTotales(antigua)
	diasNueva = diasTotales(nueva)
	if diasNueva > diasAntigua:
		difernecia = diasNueva - diasAntigua 
	else:
		difernecia = diasAntigua - diasNueva
	return difernecia
print()
print(diferneciaFecha(nueva,antigua))
