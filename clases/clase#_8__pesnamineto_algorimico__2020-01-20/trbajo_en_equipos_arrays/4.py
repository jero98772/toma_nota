
def entredatosarrreglos(size):
	larry = []
	for i in range(size):
		i = input("array input")
		larry.append(i)
	return larry
def tercerarreglo():
	
	size = 2
	en1 = entredatosarrreglos(size)
	en2 = entredatosarrreglos(size)

	arreglo = en1+en2
	return arreglo#[1,3,4,2]
def voltear(arreglo):
	for i,j in zip(arreglo,range(len(arreglo))):
		arreglo[-1*j] = i
	return arreglo[::-1]
def cambiar(arreglo):
	tamaño = len(arreglo)
	mitad1 = arreglo[-1*int(tamaño/2):]
	mitad2 = arreglo[:int(tamaño/2)]
	return mitad1, mitad2
def invertircadaudo():
	er3 = tercerarreglo()
	m,m2=cambiar(er3)
	m = voltear(m)
	m2 = voltear(m2)
	return m,m2

m,m2= invertircadaudo()
print(m,m2)
"""
4. Hace un programa que entre datos para dos arreglos de igual tamaño y que 
forme un tercer arreglo mediante el producto de los elementos de los dos 
arreglos tomados en orden inverso; es decir, un tercer arreglo que contenga el 
producto del primer elemento del primer arreglo por el último del segundo, el
del segundo del primer arreglo por el primero del segundo arreglo.
Muestre el arreglo formado.
1[0]=2[u]
......... no dice
2[0]=2[1]
"""