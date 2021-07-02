#1
def nummayor(vector): 
	mayor = 0
	for i in vector : 
	   if i == 0 :
	       mayor = i
	   if mayor < i:
	       mayor = i
	return mayor       
vector=[1,2,3,2,5,14,1,5,11,3,2,12]
#2
def buscar():
	vector=["perro","pez","pajaro","pejelagarto"]
	elemento = input("introdusca el valor a puscar en "+ str(vector))
	if elemento  in vector :
	  print(vector.index(elemento ))
	  exit()
#3
def invertirV(V):
	return V[::-1]	  
print(nummayor(vector))
print(invertirV([1,2,3,2,5,14,1,5,11,3,2,12]))
#buscar()
#4
def promedioV(V):
	suma = 0
	for i in V:
		suma +=i 
	promedio = suma/len(V)  
	return promedio
print(promedioV([1,2,3,2,5,14,1,5,11,3,2,12]))
#5
def sumV(V0,V1):
	V = []
	if len(V0) == len(V1):
		for i0,i1 in zip(V0,V1):
			V.append(i0+i1)
	return V
print(sumV([2,2],[2,2]))
#6
def vec1o0(V):
	vector = []
	for i in V:
		if i%2 == 0:
			vector.append(0)
		else:
			vector.append(1)
	return vector	
print(vec1o0([1,2,3,2,5,14,1,5,11,3,2,12]))
#7
def persona(nombres,edades,esturas):
	nombreMenedad = ""
	nombreMayalto = ""

	if len(nombres) == len(edades) and len(edades) ==len(esturas):
		for i1,i2,i3,i in zip(nombres,edades,esturas,range(len(nombres))):
		   if i==0:
		   		edadMen=i2
		   		esturasMay=i3
		   		nombreMenedad = i1
		   		nombreMayalto = i1
		   if esturasMay < i3:#estaura
		       esturasMay = i3
		       nombreMayalto = i1
		   if edadMen > i2:#edades
		       edadMen = i2
		       nombreMenedad = i1
		return nombreMayalto,nombreMenedad 
	else:
		return "no tiene el mismo tamaño"
		   	
print(persona(["dada","dede","didi","dodo"],[11,33,55,1],[1.34,2.13,3.22,0.53]))