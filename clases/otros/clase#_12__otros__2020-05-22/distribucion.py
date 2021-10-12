def repartir():
	aforo=5
	informes=10
	estudianteNombre=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
	estudiantes=len(estudianteNombre)	
	listas=[]
	personas=""
	repartir=0
	for i in range(0,aforo*informes+1):
		print([repartir])
		if i%aforo==0:
			listas.append(personas)
			personas=""
		repartir=i%estudiantes
		personas+=","+estudianteNombre[repartir]
	print(listas)
repartir()