def entredatosarrreglos(size):
	larry = []
	for i in range(size):
		i = i#input("array input")
		larry.append(i)
	return larry
def tercerarreglo(size):
	en1 = entredatosarrreglos(size)
	en2 = entredatosarrreglos(size)

	arreglo = en1+en2
	return arreglo
#def voltear(arreglo):
	for i,j in zip(arreglo,range(len(arreglo))):
		#print(j,i)
		arreglo[:-1*j] = i
	return arreglo
#voltear(tercerarreglo())
#primer elemento del primer arreglo por el último del segundo, el del segundo del primer arreglo por el primero del segundo arreglo
er3 = tercerarreglo()
print(er3)
print(voltear(er3))