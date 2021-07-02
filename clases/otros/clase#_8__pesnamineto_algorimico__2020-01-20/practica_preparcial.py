mejoressedes = "\n"
sumaSedes = 0
bebescerdos = 0
mascerdosadultos = 0
for i in range(2):
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