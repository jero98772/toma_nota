def cerdos():
	cadasede = 24
	mejoressedes = "\n"
	sumaSedes = 0
	bebescerdos = 0
	mascerdosadultos = 0
	for i in range(cadasede):
		nombreSede = str(input("Ingrese el nombre de la Sede: "))
		machos = int(input("Ingrese el  numero de cerodos machos adultos: "))
		hembras = int(input("Ingrese el  numero de cerodos hembras adultos: "))
		cerdosde6 = int(input("Ingrese el  numero de cerodos menores a 6 meses: "))
		dinero = int(input("Ingrese el  numero de ingresos anuales: "))
		cerdostotales = cerdosde6 + machos + hembras
		cerdosadultos = machos + hembras
		if cerdostotales > 1000 and dinero < 250000000:
			mejoressedes = nombreSede + "\n"  
		if cerdosadultos > mascerdosadultos or i == 0: 
			cerodosPorsede = nombreSede + "  tiene mas cerdos que las otras sedes con un total de " + str(cerdosadultos) 
		if hembras < machos:
			sumaSedes = sumaSedes + dinero
		bebescerdos = bebescerdos +  cerdosde6 
	print(f"las sedes \n {mejoressedes} \n  que tiene mas de 1000 cerdos y menos de 250000000")
	print(cerodosPorsede)
	promedio = sumaSedes/24 
	print(f"{ promedio } el promedio de  las sedes con menos hembras")
	porcentaje = cerdostotales*bebescerdos/cerdostotales
	print(f"porcentaje de cerdos totales con comparacion a los cerodos menores a 6 meses es {porcentaje}")
cerdos()
"""
Los animales de granja son especies domesticadas por el hombre que
tradicionalmente
son criados en un entorno rural. En general, se puede decir que el hombre selecciona y
cría este tipo de animales tanto para consumo humano como para otros propósitos. En
particular, “la granja del tío Jose” es muy reconocida por la calid
ad de la crianza de cerdos.
Esta granja cuenta con 24 sedes alrededor del país y por cada sede se pide la siguiente
información:

El nombre de la sede

EL número de machos adultos

El número de hembras adultas

El número de cerdos que tienen menos de 6 mes nac
idos

El monto de dinero por las ventas anuales de la sede
Usted debe hacer un algoritmo que de acuerdo con la información ingresada por cada
sede de la granja determine:

La cantidad de sedes que tienen una población mayor a 1000 cerdos pero que tienen
ve
ntas anua
les menores a 250’000.000.

La sede que tiene el menor n
úmero de animales adultos.

El promedio de ventas anuales para las sedes que tien
en más hembras que machos.

El porcentaje del total de cerdos con menos de 6 meses con respecto a la po
blación
total de animales.
"""