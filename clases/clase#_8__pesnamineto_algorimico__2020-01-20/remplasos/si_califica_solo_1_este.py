def reemplazar(base,reemplazar,replaso):#en la que se va a palabra a reemplazar, palabra a reemplazar,  replaso

	lbase = list(base)
	reemplazar = list(reemplazar)
	capusla = []
	counter = 0
	length = len(base)
	capusla.append(replaso)
	palabra = ""
	for count,i,j,k in zip(range(len(base)),base,reemplazar,replaso):
		
		if i == j  :
			print(i,j,"pasa")
			base.remove(j)
			puesto = count
			base[puesto] = capusla
	for string in base:
			palabra += string	
	
	return palabra
base = "no soy capas"
frase = reemplazar(base,"no "," ")
print(frase)
