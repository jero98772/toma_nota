#falta el proceso para las claves
dicc = "dien malcugros"
texto = "un mercenario"
n = 21
e = 11
d = 11
nuevotexto = [] 
enctext = []
encdicc = []
nuevodicc = []
for i in texto:
	nuevotexto.append(i)
print(nuevotexto)
for i in dicc:
	nuevodicc.append(i)
#print(nuevodicc)
#encriptar
for i in  range(len(nuevotexto)):
	newpos = ((i**e)%n)
	enctext.append(newpos)
print(enctext,len(enctext))
#desencriptar
for i in range(len(enctext)):
	newpos2 = (enctext[i]**e)%n
	#encdicc.append(nuevodicc[newpos2])
	encdicc.append(nuevodicc[newpos2])
print(encdicc)
print((3**11)%21)
